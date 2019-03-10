from django.urls import path
from galerie import views

app_name='galerie'

urlpatterns=[
    path('',views.index_galerie,name="index_galerie"),
]
