from django.contrib import admin

# Register your models here.

from .models import Tasks
from .models import Update

admin.site.register(Tasks)
admin.site.register(Update)
