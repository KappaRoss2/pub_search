from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('parser', views.get_article, name="get_article"),
]