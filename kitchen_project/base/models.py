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
  # checked = models.BooleanField(null=True)
  subject = models.CharField(max_length=200)
  description = models.TextField()
  type = models.CharField(max_length=6, choices=update_types)

  def __str__(self):
    return self.subject

class Inventory(models.Model):
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  storage_locations = (
    ('Dry', 'Dry'),
    ('Frozen', 'Frozen'),
    ('Walkin', 'Walkin'),
    ('Lowboy', 'Lowboy'),
  )
  located = models.CharField(max_length=6, choices=storage_locations)
  to_whiteboard = models.BooleanField(null=True)
  name = models.CharField(max_length=200)
  par = models.CharField(max_length=200)
  on_hand = models.CharField(max_length=200, null=True)
  exp_date = models.CharField(max_length=200, null=True)
  flag_choices = (
    ('Low', 'Low'),
    ('Out', 'Out'),
    ('Dead', 'Dead'),
    ('Expiring', 'Expiring'),
  )
  flag = models.CharField(max_length=8, choices=flag_choices, null=True)

  def __str__(self):
    return self.name
