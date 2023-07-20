from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_screen, name='start_screen'),
]