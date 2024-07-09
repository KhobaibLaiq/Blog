from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogapp/blog_list.html', context)

@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all()
    if request.method == 'POST':
        # if not request.user.is_authenticated:
        #     return HttpResponseForbidden("You must be logged in to comment.")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()

            # Return JSON response with comment details
            return JsonResponse({
                'author': comment.author.username,
                'text': comment.text,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format datetime as string
            })

    else:
        form = CommentForm()
    return render(request, 'blogapp/blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogapp/create_blog.html', {'form': form})

@login_required
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this blog")
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/update_blog.html', {'form': form})

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog")
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blogapp/delete_blog.html', {'blog': blog})
