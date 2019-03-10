from django.shortcuts import render
from .models import Event
# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")

def index_evenements(request):
    events=Event.objects.all().order_by('date')
    index_evenements={
    'welcome2':'Bienvenue au Evénements du Club ',
    'clubname':'Hexa24Club',
    'events':events
    }
    return render(request,"index_evenements.html",context=index_evenements)
