from django import forms
from .models import PostModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ admin để mở khóa.",
                code='inactive',
            )