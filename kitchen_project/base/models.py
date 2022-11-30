from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  # user =
  shift_lists = (
    ('Opening', 'Opening'),
    ('Closing', 'Closing'),
    ('Mid', 'Mid')
  )
  shift = models.CharField(max_length=7, choices=shift_lists)
  name = models.CharField(max_length=200)
  checked = models.BooleanField(null=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Update(models.Model):
  # user =
  update_types = (
    ('NEW', 'NEW'),
    ('OUT', 'OUT'),
    ('GONE', 'GONE'),
    ('CHANGE', 'CHANGE'),
  )
  type = models.CharField(max_length=6, choices=update_types)
  subject = models.CharField(max_length=200)
  description = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.subject

class Inventory(models.Model):
  # user =
  storage_locations = (
    ('Dry', 'Dry'),
    ('Frozen', 'Frozen'),
    ('Walkin', 'Walkin'),
    ('Lowboy', 'Lowboy'),
  )
  located = models.CharField(max_length=6, choices=storage_locations)
  flag_choices = (
    ('Low', 'Low'),
    ('Out', 'Out'),
    ('Dead', 'Dead'),
    ('Expiring', 'Expiring'),
  )
  flag = models.CharField(max_length=8, choices=flag_choices, blank=True)
  to_whiteboard = models.BooleanField(null=True)
  name = models.CharField(max_length=200)
  par = models.CharField(max_length=200)
  on_hand = models.CharField(max_length=200, blank=True)
  exp_date = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Prep(models.Model):
  # user =
  menu_headings = (
    ('Appetizers', 'Appetizers'),
    ('Entrees', 'Entrees'),
    ('Sides', 'Sides'),
    ('Desserts', 'Desserts'),
  )
  heading = models.CharField(max_length=10, choices=menu_headings, blank=True)
  flag_choices = (
    ('Low', 'Low'),
    ('Out', 'Out'),
    ('Dead', 'Dead'),
    ('Expiring', 'Expiring'),
  )
  flag = models.CharField(max_length=8, choices=flag_choices, blank=True)
  to_whiteboard = models.BooleanField(null=True)
  name = models.CharField(max_length=200)
  par = models.CharField(max_length=200)
  on_hand = models.CharField(max_length=200, blank=True)
  exp_date = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  in_use = models.BooleanField()
  component_of = models.TextField()
  details = models.TextField(blank=True)
  # images =

  # component_of = reference recipe card?
  # HOW TO LINK TO RECIPE CARD? DROPDOWN WITH ALL MENU ITEMS? MAYBE MAKE A DISH CLASS AND LINK TO ALL? OR RECIPE? OR MAKE MENU HEADINGS/MENU ITEMS DICTIONARIES IN GLOBAL SCOPE AND REFERENCE THEM IN EACH CLASS?

  def __str__(self):
    return self.name

class Recipe(models.Model):
  # user =
  menu_headings = (
    ('Appetizers', 'Appetizers'),
    ('Entrees', 'Entrees'),
    ('Sides', 'Sides'),
    ('Desserts', 'Desserts'),
  )
  heading = models.CharField(max_length=10, choices=menu_headings)
  # how to list as a component of multiple headings?
  dish = models.CharField(max_length=200)
  prep_tasks = models.TextField(blank=True)
  # prep_tasks = reference prep db?
  ingredients = models.TextField()
  directions = models.TextField()
  prep_time = models.CharField(max_length=200)
  cooking_time = models.CharField(max_length=200)
  batch_size = models.CharField(max_length=200)
  par = models.CharField(max_length=200, blank=True)
  shelf_life = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  in_use = models.BooleanField()
  component_of = models.TextField(blank=True)
  # images =
  # component_of = HOW TO LINK TO RECIPE CARD? DROPDOWN WITH ALL MENU ITEMS? MAYBE MAKE A DISH CLASS AND LINK TO ALL? OR RECIPE?

  def __str__(self):
    return self.dish
