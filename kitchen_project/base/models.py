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

  class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    update_types = (
      ('New', 'New'),
      ('Out', 'Out'),
      ('Gone', 'Gone'),
      ('Change', 'Change'),
    )
    checked = models.BooleanField(null=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=6, choices=update_types)

    def __str__(self):
      return self.subject
