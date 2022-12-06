from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Task, Update, Inventory, Prep, Recipe, Post
from .forms import UpdateForm


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
  return render(request, 'registration/login.html', context)


def logoutUser(request):
  logout(request)
  return redirect('/login')

def home(request):
    users = CustomUser.objects.all()
    updates = Update.objects.all()
    context = {'users': users, 'updates': updates}
    return render(request, 'home.html', context)

def checklist(request):
    # tasks = Task.objects.all()
    # context = {'tasks': tasks}
    # return render(request, 'checklist.html', context)
    return render(request, 'checklist.html')

def opening(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'opening.html', context)

def mid(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'mid.html', context)

def closing(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'closing.html', context)

def changes(request):
    updates = Update.objects.all()
    form = UpdateForm()

    if request.method == 'POST':
        # print(request.POST)
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/changes')

    context = {'updates': updates, 'form': form}
    return render(request, 'changes.html', context)

def createUpdate(request):
    updates = Update.objects.all()
    form = UpdateForm()

    if request.method == 'POST':
        # print(request.POST)
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/changes')


    context = {'updates': updates, 'form': form}
    return render(request, 'update_form.html', context)

def updateUpdate(request, pk):
    update = Update.objects.get(id=pk)
    form = UpdateForm(instance=update)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/changes')

    context = {'form': form}
    return render(request, 'update_form.html', context)

def deleteUpdate(request, pk):
    update = Update.objects.get(id=pk)
    if request.method == 'POST':
        update.delete()
        return redirect('/changes')
    return render(request, 'delete.html', {'obj':update})

def inventory(request):
    items = Inventory.objects.all()
    # sort_by_location = Inventory.object.filter(title='located').order_by('Dry', 'Frozen', 'Lowboy', 'Walkin')
    context = {'items': items}
    return render(request, 'inventory.html', context)

def prep(request):
    todos = Prep.objects.all()
    context = {'todos': todos}
    return render(request, 'prep.html', context)

def recipes(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    cards = Recipe.objects.filter(
        Q(prep_tasks__icontains=q) |
        Q(heading__icontains=q) |
        Q(dish__icontains=q)
    )
    # cards = Recipe.objects.all()
    todos = Prep.objects.all()
    context = {'cards': cards, 'todos': todos}
    return render(request, 'recipes.html', context)

def dish(request, pk):
    recipe_number = Recipe.objects.get(id=pk)
    recipe_number = str(recipe_number)
    cards = Recipe.objects.all()
    todos = Prep.objects.all()
    context = {'recipe_number': recipe_number, 'cards': cards, 'todos': todos}
    return render(request, 'card.html', context)

def whiteboard(request):
    items = Inventory.objects.all()
    todos = Prep.objects.all()
    context = {'items': items, 'todos': todos}
    return render(request, 'whiteboard.html', context)
