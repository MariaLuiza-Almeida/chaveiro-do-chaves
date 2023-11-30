from .views import getKeys, createKey, menu, editKeys, updateKey, update, delete, getKeysByName
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', menu, name='menu'),
    path('getKeys/', getKeys, name='getKeys'),
    path('getKeysByName/', getKeysByName, name='getKeysByName'),
    path('createKey/', createKey, name='createKey'),
    path ('editKeys/', editKeys, name='editKeys' ),
    path('updateKey/<int:id>', updateKey, name='updateKey'), 
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]