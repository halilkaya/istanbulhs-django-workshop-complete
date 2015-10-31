# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from app.models import Category, Post

def index(request):
    data = {
        'posts': Post.objects.order_by('-created_at'),
    }
    return render(request, 'index.html', data)

def post_single(request, post_slug):
    data = {
        'post': Post.objects.get(slug=post_slug)
    }
    return render(request, 'post_single.html', data)
