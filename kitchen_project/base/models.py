from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Task(models.Model):
  user = models.ForeignKey(CustomUser, related_name='task', on_delete=models.SET_NULL, null=True)
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
  user = models.ForeignKey(CustomUser, related_name='update', on_delete=models.SET_NULL, null=True)
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

  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.subject

class Post(models.Model):
  title = models.CharField(max_length=69)
  body = models.TextField(max_length=666)
  user = models.ForeignKey(CustomUser, related_name='post', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(null=True)

  def __str__(self):
    return f'{self.title} - {self.created}'

  class Meta:
    ordering = ['-created']

  def get_absolute_url(self):
    return reverse('base:home', args=(self.pk,))

class Inventory(models.Model):
  user = models.ForeignKey(CustomUser, related_name='inventory', on_delete=models.SET_NULL, null=True)
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
  need = models.CharField(max_length=200, blank=True)
  exp_date = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Recipe(models.Model):
  user = models.ForeignKey(CustomUser, related_name='recipe', on_delete=models.CASCADE, null=True)
  menu_headings = (
    ('Appetizers', 'Appetizers'),
    ('Entrees', 'Entrees'),
    ('Sides', 'Sides'),
    ('Desserts', 'Desserts'),
  )
  heading = models.CharField(max_length=10, choices=menu_headings)
  dish = models.CharField(max_length=200)
  prep_tasks = models.ManyToManyField('Prep', through='RecipeTasks', blank=True)
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


  def __str__(self):
    return self.dish


class Prep(models.Model):
  user = models.ForeignKey(CustomUser, related_name='prep', on_delete=models.SET_NULL, null=True)
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
  need = models.CharField(max_length=200, blank=True)
  exp_date = models.CharField(max_length=200, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  in_use = models.BooleanField()
  details = models.TextField(blank=True)
  task_for = models.ManyToManyField('Recipe', through='RecipeTasks', blank=True)

  # class Meta:
  #   ordering = ['task_for']

  def __str__(self):
    return self.name

class RecipeTasks(models.Model):
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
  prep = models.ForeignKey(Prep, on_delete=models.CASCADE, blank=True)

  def __str__(self):
    return f'{self.recipe} - {self.prep}'
