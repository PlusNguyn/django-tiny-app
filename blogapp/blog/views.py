from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm
from django.core.paginator import Paginator
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426

def index(request):
    posts = PostModel.objects.all()
    page = Paginator(posts, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()

    context = {
                # 'posts': posts,
               'form': form,
               'page': page}
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.pk)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'form': form,
        'post': post
        }
    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }  
    return render(request, 'blog/post_delete.html', context)
<<<<<<< HEAD
<<<<<<< HEAD

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        username = self.request.POST.get('username')  # Lấy username từ request
        user = User.objects.filter(username=username).first()

        # Xóa lỗi mặc định của Django trong form.errors
        form.errors.pop("__all__", None)

        if user and not user.is_active:
            messages.error(self.request, "Tài khoản của bạn đã bị khóa.")
        else:
            messages.error(self.request, "Tên đăng nhập hoặc mật khẩu không đúng.")

        return super().form_invalid(form)

def unlock_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, "Tài khoản của bạn đã được mở khóa. Vui lòng tải lại trang và thử đăng nhập lại.")
    return redirect('login')
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
