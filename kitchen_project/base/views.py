from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from .models import Update

def home(request):
    return render(request, 'home.html')

def checklist(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'checklist.html', context)

def whiteboard(request):
    return render(request, 'whiteboard.html')

# def changes(request):
#     return render(request, 'changes.html')

def changes(request):
    updates = Update.objects.all()
    context = {'updates': updates}
    return render(request, 'changes.html', context)

def inventory(request):
    return render(request, 'inventory.html')

def prep(request):
    return render(request, 'prep.html')

def recipes(request):
    return render(request, 'recipes.html')
