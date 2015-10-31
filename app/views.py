# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from app.models import Category, Post

def index(request):
    data = {
        'posts': Post.objects.order_by('-created_at').filter(is_page=False),
    }
    return render(request, 'index.html', data)

def post_single(request, post_slug):
    data = {
        'post': Post.objects.get(slug=post_slug)
    }
    return render(request, 'post_single.html', data)

def page(request, page_slug):
    data = {
        'post': Post.objects.get(slug=page_slug)
    }
    return render(request, 'page.html',data)

def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.order_by('-created_at').filter(category=category,is_page=False)

    return render(request, 'category.html', { 'category_posts': posts, 'category_single': category })
