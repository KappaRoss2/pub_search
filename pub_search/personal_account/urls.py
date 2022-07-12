from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tabs/', views.get_tabs, name="get_tabs"),
]