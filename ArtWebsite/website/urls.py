from django.contrib import admin
from django.urls import path
from .views import artPage, home

urlpatterns = [
    path('art', artPage, name="artpage"),
    path('', home, name="homepage")
]
