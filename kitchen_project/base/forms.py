from django.forms import ModelForm
from .models import Update, Task, Inventory, Prep, Recipe

class UpdateForm(ModelForm):
  class Meta:
    model = Update
    # fields = '__all__'
    fields = ['type', 'subject', 'description']

class TaskForm(ModelForm):
  class Meta:
    model = Task
    # fields = '__all__'
    fields = ['checked']

class InventoryForm(ModelForm):
  class Meta:
    model = Inventory
    fields = '__all__'

class PrepForm(ModelForm):
  class Meta:
    model = Prep
    fields = '__all__'

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = '__all__'
