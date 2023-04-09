from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def register(request):
    return render(request, 'main/register.html')




def about(request):
    return render(request, 'main/about.html')
