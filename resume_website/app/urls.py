from django.urls import path
from django.shortcuts import render

from app import views

urlpatterns = [

    path("",views.index,name="index"),
]