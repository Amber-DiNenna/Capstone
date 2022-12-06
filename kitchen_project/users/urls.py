from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/login/', views.loginPage, name='login'),
    path('registration/login/', views.logoutUser, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile')
]
