from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'home.html', context)

def changes(request):
    return render(request, 'changes.html')

def inventory(request):
    return render(request, 'inventory.html')

def prep(request):
    return render(request, 'prep.html')

def whiteboard(request):
    return render(request, 'whiteboard.html')

def checklist(request):
    return render(request, 'checklist.html')

def recipes(request):
    return render(request, 'recipes.html')
