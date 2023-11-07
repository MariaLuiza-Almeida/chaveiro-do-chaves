from .views import home, salvar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('', home, name='home'),
path ('/salvar', salvar, name='salvar')
]