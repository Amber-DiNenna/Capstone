from django.db import models

class Checklist(models.Model):
  # user =
  # timestamp = models.DateTimeField
  # clear =
  # shift =
  # participants
  name = models.CharField(max_length=200)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  # shift_lists = (
  #   ('Opening'),
  #   ('Closing'),
  # )
  checked = models.BooleanField(null=True)
  task = models.CharField(max_length=200)
  # shift = models.CharField(max_length=1, choices=shift_lists)

  def __str__(self):
    return self.name
