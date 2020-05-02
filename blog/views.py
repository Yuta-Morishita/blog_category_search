from django.shortcuts import render, get_object_or_404
from .models import Category, Blog


def index(request):
    blog = Blog.objects.order_by('-id')
    return render(request, 'blog/index.html', {'blog': blog})


def category(request, category):
    category = Category.objects.get(name=category)
    blog = Blog.objects.filter(category=category)
    return render(request, 'blog/index.html',
                  {'category': category, 'blog': blog})


def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog_text': blog_text})
