from django.shortcuts import render
from .models import Project
# Create your views here.
def index_projets(request):
    projs=Project.objects.all()
    index_projets={
    'welcome':'Bienvenue au Projets du Club ',
    'clubname':'Hexa24Club',
    'projs':projs
    }
    return render(request,"index_projets.html",context=index_projets)
