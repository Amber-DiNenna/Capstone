from django.shortcuts import render
from .models import Update
from django.views.generic import ListView

# Create your views here.

# class ListPosts(ListView):
#     model = Update
#     template_name = 'home.html'

# def changes(request):
#     change = Update.objects.all()
#     context = {'change': change}
#     return render(request, 'changes.html', context)
