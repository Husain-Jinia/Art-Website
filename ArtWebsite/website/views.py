from django.shortcuts import render
from models import Art
# Create your views here.

def ArtPage(request):
    art = Art.objects.all()
    return render(request,'artPage.html',art)