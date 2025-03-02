from django import forms
from .models import PostModel
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['title', 'content']

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ admin để mở khóa.",
                code='inactive',
            )
=======
        fields = ['title', 'content']
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
        fields = ['title', 'content']
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
