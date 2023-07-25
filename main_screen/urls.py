from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.start_screen, name='main'),
    path('profile/', views.profile, name='profile'),
    path('shop/', views.shop, name='shop'),
    path('inventory/', views.inventory, name='inventory'),
    path('shop/purchase/<int:item_id>/', views.purchase_item, name='purchase_item'),
    path('start_game/', views.start_game, name='start_game'),
]