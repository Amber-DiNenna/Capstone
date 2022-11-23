from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'home.html', context)
