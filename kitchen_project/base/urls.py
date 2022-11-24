from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('changes/', views.changes, name='changes'),
    path('inventory/', views.inventory, name='inventory'),
    path('prep/', views.prep, name='prep'),
    path('whiteboard/', views.whiteboard, name='whiteboard'),
    path('checklist/<str:pk>/', views.checklist, name='checklist'),
    path('recipes/', views.recipes, name='recipes'),
]
