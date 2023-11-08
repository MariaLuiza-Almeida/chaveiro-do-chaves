from .views import getKeys, createKey
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', getKeys, name='getKeys'),
    path('createKey/', createKey, name='createKey'),
]