from django.urls import path
from tomatoes.models import start_the_game

urlpatterns = [
    path('', start_the_game(), name='tomatoes'),
]