from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path("", views.blog_index, name='index'),
    path("<int:pk>/", views.blog_detail, name='detail'),
    path("<category>/", views.blog_category, name='category')
]