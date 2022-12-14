from django.shortcuts import render, redirect
from users.models import CustomUser
from django.db.models import Q
from .models import Task, Update, Inventory, Prep, Recipe, RecipeTasks
from .forms import UpdateForm, TaskForm

def home(request):
    users = CustomUser.objects.all()
    updates = Update.objects.all()
    context = {'users': users, 'updates': updates}
    return render(request, 'home.html', context)

def checklist(request):
    return render(request, 'checklist.html')

def opening(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/checklist/opening/')

    context = {'tasks': tasks, 'form': form}
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
    recipe_tasks = RecipeTasks.objects.all()
    context = {'todos': todos, 'recipe_tasks': recipe_tasks}
    return render(request, 'prep.html', context)

def recipes(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    cards = Recipe.objects.filter(
        # Q(prep_tasks__icontains=q) |
        Q(heading__icontains=q) |
        Q(dish__icontains=q)
    )
    cards = Recipe.objects.all()
    todos = Prep.objects.all()
    context = {'cards': cards, 'todos': todos}
    return render(request, 'recipes.html', context)

def dish(request, pk):
    recipe_number = Recipe.objects.get(id=pk)
    recipe_number = str(recipe_number)
    cards = Recipe.objects.all()
    todos = Prep.objects.all()
    recipe_tasks = RecipeTasks.objects.all()
    context = {'recipe_number': recipe_number, 'cards': cards, 'todos': todos, 'recipe_tasks': recipe_tasks}
    print('!!!!!!!!!!!!!!!!', context)
    return render(request, 'card.html', context)

def whiteboard(request):
    items = Inventory.objects.all()
    todos = Prep.objects.all()
    context = {'items': items, 'todos': todos}
    return render(request, 'whiteboard.html', context)

def HomeRegister(request):
    if len(request.POST['password']) < 8:
        return redirect('base:home')
    if request.POST['password2'] == request.POST['password']:
        user_model = CustomUser(username=request.POST['name'], password=(request.POST['password']))
        user_model.save()
    else:
        print("not match")

    return redirect('base:home')









# def loginPage(request):

#     # if request.user.is_authenticated:
#     #     return redirect('/')

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#     try:
#         user = CustomUser.objects.get(username=username)
#     except:
#         messages.error(request, 'Username does not exist.')

#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
#         return redirect('/')
#     else:
#         messages.error(request, 'Username or password does not exist.')

#     context = {}
#     return render(request, 'registration/login.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('/login')
