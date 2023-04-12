from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView
from .models import Fuel
from django.shortcuts import render


# def index(request):
#     return render(request, 'main/index.html',)


def register(request):
    return render(request, 'main/register.html')


class HomeView(View):
    def get(self, request):
        fuels = Fuel.objects.all()
        return render(request, "main/index.html", {"fuel_list": fuels})

class FuelView(DetailView):
    model = Fuel
    template_name = 'datail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'detail'
    
