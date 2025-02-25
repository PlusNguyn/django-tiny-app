from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
