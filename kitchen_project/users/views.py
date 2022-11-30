from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


# Create your views here.



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
