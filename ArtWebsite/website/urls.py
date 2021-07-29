from django.contrib import admin
from django.urls import path
from .views import artPage

urlpatterns = [
    path('', artPage, name="artpage")
]
