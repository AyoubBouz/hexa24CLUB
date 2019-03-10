from django.urls import path
from projets import views

app_name='projets'

urlpatterns=[
    path('',views.index_projets,name="index_projets"),
]
