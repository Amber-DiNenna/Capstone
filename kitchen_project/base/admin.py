from django.contrib import admin

# Register your models here.

from .models import Tasks
from .models import Update
from .models import Inventory
from .models import Prep
from .models import Recipe

admin.site.register(Tasks)
admin.site.register(Update)
admin.site.register(Inventory)
admin.site.register(Prep)
admin.site.register(Recipe)
