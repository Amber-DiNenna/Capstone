from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from .models import Update
from .models import Inventory
from .models import Prep
from .models import Recipe

def home(request):
    return render(request, 'home.html')

def checklist(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'checklist.html', context)

def changes(request):
    updates = Update.objects.all()
    context = {'updates': updates}
    return render(request, 'changes.html', context)

def inventory(request):
    items = Inventory.objects.all()
    context = {'items': items}
    return render(request, 'inventory.html', context)

def prep(request):
    todos = Prep.objects.all()
    context = {'todos': todos}
    return render(request, 'prep.html', context)

def recipes(request):
    cards = Recipe.objects.all()
    context = {'cards': cards}
    return render(request, 'recipes.html', context)

def whiteboard(request):
    items = Inventory.objects.all()
    todos = Prep.objects.all()
    context = {'items': items, 'todos': todos}
    return render(request, 'whiteboard.html', context)
