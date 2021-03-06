
from .models import Category, Tag, Blog
from django.views import generic


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        queryset = Blog.objects.order_by('-id')
        return queryset


class CategoryView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Blog.objects.order_by('-id').filter(category=category)
        return queryset
    """ アクセスされた値を取得し辞書に格納 """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        return context


class TagView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        tag = Tag.objects.get(name=self.kwargs['tag'])
        queryset = Blog.objects.order_by('-id').filter(tag=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_key'] = self.kwargs['tag']
        return context


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
