from django.contrib import admin
from .models import Task
from .models import Update
from .models import Inventory
from .models import Prep
from .models import Recipe

admin.site.register(Task)
admin.site.register(Update)
admin.site.register(Inventory)
admin.site.register(Prep)
admin.site.register(Recipe)
