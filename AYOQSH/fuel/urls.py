from django.urls import path 
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('page/', views.page, name='page'),
    ]
