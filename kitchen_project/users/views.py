from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.

def loginPage(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = CustomUser.objects.get(username=username)
    except:
      messages.error(request, 'Username does not exist.')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.error(request, 'Username or password does not exist.')


  context = {}
  return render(request, 'users/registration/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('/login')

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  template_name = 'signup.html'
  success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUserChangeForm
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
