from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .models import Group, Post


def hello(request):
    template = 'test_app/index.html'
    result = 16
    context = {
        'template_var': result,
        'numbers': [1, 2, 3, 4],
    }
    return render(request, template, context)

# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups-1
# Entry.objects.get(headline__icontains='Lennon')
# SELECT ... WHERE headline ILIKE '%Lennon%';

def posts_list(request):
    template = 'test_app/posts_list.html'
    posts = Post.objects.all()
    # posts = Post.objects.filter(text='Hi')
    # posts = Post.objects.filter(text__contains='H')
    # posts = Post.objects.filter(text__icontains='h')
    # posts = Post.objects.filter(text__startswith='h')
    context = {
        "posts": posts,
    }
    return render(request, template, context)


class PostListView(ListView):
    model = Post


def post_detail(request, post_id):
    template = 'test_app/post_info.html'
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "post": post,
    }
    return render(request, template, context)


def groups_list(request):
    template = 'test_app/groups_list.html'
    groups = Group.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, template, context)


def group_posts(request):
    pass