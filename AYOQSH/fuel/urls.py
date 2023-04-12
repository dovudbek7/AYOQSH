from django.urls import path 
from .import views
from .views import FuelView

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path("<slug:slug>/", views.FuelView.as_view(), name="detail")
]
