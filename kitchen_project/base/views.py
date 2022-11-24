from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks

# checklists = [
#     {'id':1, 'name': 'Opening Checklist'},
#     {'id':2, 'name': 'Closing Checklist'},
# ]

def home(request):
    # checklists = Tasks.objects.all()
    # context = {'checklists': checklists}
    return render(request, 'home.html')

# def checklist(request, pk):
    # checklist = None
    # for i in checklists:
    #     if i['id'] == int(pk):
    #         checklist = i
def checklist(request):
    # checklist = Tasks.objects.get('shift')
    # context = {'checklist': checklist}
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'checklist.html', context)

def changes(request):
    return render(request, 'changes.html')

def inventory(request):
    return render(request, 'inventory.html')

def prep(request):
    return render(request, 'prep.html')

def whiteboard(request):
    return render(request, 'whiteboard.html')

def recipes(request):
    return render(request, 'recipes.html')
