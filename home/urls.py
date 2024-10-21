

# home/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('repair/', views.repair_page, name='repair_page'),

    
]
