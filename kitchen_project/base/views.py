from django.shortcuts import render
from django.http import HttpResponse
from .models import Checklist

# checklists = [
#     {'id':1, 'name': 'Opening Checklist'},
#     {'id':2, 'name': 'Closing Checklist'},
# ]

def home(request):
    checklists = Checklist.objects.all()
    context = {'checklists': checklists}
    return render(request, 'home.html', context)

def checklist(request, pk):
    # checklist = None
    # for i in checklists:
    #     if i['id'] == int(pk):
    #         checklist = i
    checklist = Checklist.objects.get(id=pk)
    context = {'checklist': checklist}
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
