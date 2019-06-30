from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment, Tag
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django_user_agents.utils import get_user_agent
import re
import random

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date',) #'-' order by DESC
    context = {
        'posts': posts,
        'title': "Welcome to my blog" ,
    }
    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile or user_agent.is_tablet:
    #     return render(request,'blog/mobile.html', {'posts': posts} )
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    obj = Post.objects.get(id=pk)
    imagesLinkStr = obj.text.replace('"', ',')
    imagesLinkList = re.findall(r'https*://i.imgur.com/*\w*\.(?:jpg|gif|png)', imagesLinkStr)
    context = {
        'post': post,
        'title': obj.title,
        'image': random.choice(imagesLinkList),
        'description': obj.description,
    }
    return render(request, 'blog/post_detail.html', context )

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request,pk):
   u = Post.objects.get(pk=pk).delete()
   return redirect('post_list')

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def tag_view(request, name):
    tag = Tag.objects.get(name=name)
    posts = tag.posts.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

