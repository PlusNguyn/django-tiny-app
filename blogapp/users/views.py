from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from blog.models import PostModel
<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import get_object_or_404
from django.contrib import messages
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'users/sign_up.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    post_uploaded = PostModel.objects.filter(author=request.user)



    context = {
        'u_form': u_form,
        'p_form': p_form,
        'post_uploaded': post_uploaded
    }
    return render(request, 'users/profile.html', context)

<<<<<<< HEAD
<<<<<<< HEAD
def delete_selected_posts(request):
    if request.method == "POST":
        post_ids = request.POST.get("selected_posts", "").split(",")
        PostModel.objects.filter(id__in=post_ids, author=request.user).delete()
        messages.success(request, "Bài viết đã được xoá thành công!")
        return redirect("users-profile")
    
=======

>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======

>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
# from django.shortcuts import render
# from blog.models import PostModel

# def profile_view(request):
#     posts = PostModel.objects.filter(author=request.user)
#     return render(request, 'users/profile.html', {'posts': posts})
