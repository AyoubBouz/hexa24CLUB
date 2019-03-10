from django.shortcuts import render
from .models import Image


# Create your views here.
def index_galerie(request):
    imgs=Image.objects.all()
    index_galerie={
    'Tsawer':'Bienvenue au Galerie du Club ',
    'clubname':'Hexa24Club',
    'imgs':imgs
    }
    return render(request,"index_galerie.html",context=index_galerie)
