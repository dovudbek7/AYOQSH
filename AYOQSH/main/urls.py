from django.urls import path 
from .import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
