from django.shortcuts import render
from .models import Art
# Create your views here.

def artPage(request):
    art = Art.objects.all()
    return render(request,'artPage.html',{'arts':art})

def home(request):
    return render(request, 'homePage.html')