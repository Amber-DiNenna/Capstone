from django.contrib import admin

# Register your models here.

from .models import Tasks
from .models import Update
from .models import Inventory

admin.site.register(Tasks)
admin.site.register(Update)
admin.site.register(Inventory)
