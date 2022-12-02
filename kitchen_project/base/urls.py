from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('changes/', views.changes, name='changes'),
    path('inventory/', views.inventory, name='inventory'),
    path('prep/', views.prep, name='prep'),
    path('whiteboard/', views.whiteboard, name='whiteboard'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<str:pk>/', views.dish, name='dish'),
    path('checklist/', views.checklist, name='checklist'),
    path('checklist/opening/', views.opening, name='opening'),
    path('checklist/mid/', views.mid, name='mid'),
    path('checklist/closing/', views.closing, name='closing'),
]
