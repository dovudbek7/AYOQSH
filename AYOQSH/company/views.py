from django.shortcuts import render
from django.views.generic.base import View
from .models import Fuel
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html',)


def register(request):
    return render(request, 'main/register.html')





