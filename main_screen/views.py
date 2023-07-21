from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Player, PlayerProfile, Achievement, Item, Shop, Inventory, InventoryItem, Settings


def start_screen(request):
    return render(request, 'start_screen.html')


def profile(request):
    player = Player.objects.get(id=1)
    player_profile = PlayerProfile.objects.get(player=player)
    achievements = player_profile.achievements.all()

    context = {
        'player': player,
        'player_profile': player_profile,
        'achievements': achievements
    }

    return render(request, 'profile.html', context)


def shop(request):
    shop = Shop.objects.get(id=1)
    items = shop.items.all()

    context = {
        'shop': shop,
        'items': items
    }

    return render(request, 'shop.html', context)


def purchase_item(request, item_id):
    item = Item.objects.get(id=item_id)
    player = Player.objects.get(id=1)  # Replace with the appropriate way to get the current player
    inventory = Inventory.objects.get(player__player=player)
    inventory_item, _ = InventoryItem.objects.get_or_create(inventory=inventory, item=item)
    inventory_item.quantity += 1  # Increment the quantity of the purchased item
    inventory_item.save()

    return redirect('inventory')  # Redirect to the inventory page


def inventory(request):
    try:
        inventory = Inventory.objects.get(player=request.user)
    except ObjectDoesNotExist:
        # Create a new inventory record for the user if it doesn't exist
        inventory = Inventory.objects.create(player=request.user)

    items = inventory.items.all()

    context = {
        'inventory': inventory,
        'items': items
    }

    return render(request, 'inventory.html', context)




def settings(request):
    player = Player.objects.get(id=1)
    settings = Settings.objects.get(player=player)

    context = {
        'player': player,
        'settings': settings
    }

    return render(request, 'settings.html', context)