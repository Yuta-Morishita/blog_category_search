from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('tag/<str:tag>/', views.TagView.as_view(), name='tag'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
