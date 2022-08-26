from django.contrib import admin
from django.urls import path, include
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.project_index, name = 'index'),
    path('<int:pk>/', views.project_detail, name = 'detail'),
    
]