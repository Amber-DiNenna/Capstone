from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    # path('registration/login/', views.loginPage, name='login'),
    # path('registration/login/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('changes/', views.changes, name='changes'),
    path('changes/create-update/', views.createUpdate, name='create-update'),
    path('changes/update-update/<str:pk>/', views.updateUpdate, name='update-update'),
    path('changes/delete-update/<str:pk>/', views.deleteUpdate, name='delete-update'),
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
