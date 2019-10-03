from django.urls import path 
from . import views

urlpatterns = [
  path('', views.index, name='home-view'),
  path('register', views.register, name='business-registration'),
]