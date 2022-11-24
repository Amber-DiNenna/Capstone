from django.db import models

class Checklist(models.Model):
  # user =
  # timestamp = models.DateTimeField
  # clear =
  # shift =
  # participants
  # updated = models.DateTimeField(auto_now=True)
  # created = models.DateTimeField(auto_now_add=True)
  checked = models.BooleanField()
  task = models.CharField(max_length=200)

  def __str__(self):
    return self.name
