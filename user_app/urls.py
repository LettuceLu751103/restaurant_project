
from django.contrib import admin
from django.urls import path, include
from .views import register, login


urlpatterns = [
    path('register/', register),
    path('login/', login)
]
