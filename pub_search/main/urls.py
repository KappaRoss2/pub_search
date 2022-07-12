from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('signup/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('parser', views.get_article, name="get_article"),
    path('parser/add/', views.add_article, name="add_article"),

]