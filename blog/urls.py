from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category>/', views.category, name='category'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
]
