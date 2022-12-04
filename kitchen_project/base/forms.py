from django.forms import ModelForm
from .models import Update

class UpdateForm(ModelForm):
  class Meta:
    model = Update
    fields = '__all__'
    # fields = ['type', 'subject', 'description']
