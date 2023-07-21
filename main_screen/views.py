from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Player, PlayerProfile, Achievement, Item, Shop, Inventory, InventoryItem, Settings
from django.contrib.auth.models import User


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
    try:
        player = Player.objects.get(user=request.user)
        shop = Shop.objects.get(player=player)
        items = shop.items.all()
    except Shop.DoesNotExist:
        shop = None
        items = None

    context = {
        'shop': shop,
        'items': items
    }

    return render(request, 'shop.html', context)


def purchase_item(request, item_id):
    item = Item.objects.get(id=item_id)
    inventory = Inventory.objects.get(player=request.user)
    if inventory.player.wallet >= item.price:
        inventory_item = InventoryItem.objects.create(inventory=inventory, item=item)
        inventory_item.save()
        # Deduct the item price from the user's wallet
        inventory.player.wallet -= item.price
        inventory.player.save()
        return redirect('inventory')
    else:
        # Handle insufficient funds error
        return redirect('shop')



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