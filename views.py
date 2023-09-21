from django.shortcuts import render, get_list_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_list_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})