from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  shift_lists = (
    ('Opening', 'Opening'),
    ('Closing', 'Closing'),
  )
  checked = models.BooleanField(null=True)
  name = models.CharField(max_length=200)
  shift = models.CharField(max_length=7, choices=shift_lists)

  def __str__(self):
    return self.name
