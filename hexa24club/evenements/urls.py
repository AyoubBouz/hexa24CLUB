from django.urls import path
from evenements import views

app_name='evenements'

urlpatterns=[
    path('',views.index_evenements,name="index_evenements"),
]
