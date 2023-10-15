from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.sign_in)
]
