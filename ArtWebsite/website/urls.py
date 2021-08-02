from django.contrib import admin
from django.urls import path
from .views import artPage, home

urlpatterns = [
    path('', artPage, name="artpage"),
    path('home', artPage, name="homepage")
]
