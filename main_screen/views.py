from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Player, PlayerProfile, Item, Shop, Inventory, InventoryItem, Settings
from django.contrib.auth.decorators import login_required


def start_screen(request):
    return render(request, 'start_screen.html')


@login_required
def profile(request):
    player = Player.objects.get(user=request.user)
    player_profile = PlayerProfile.objects.get(player=player)
    achievements = player_profile.achievements.all()

    context = {
        'player': player,
        'player_profile': player_profile,
        'achievements': achievements
    }

    return render(request, 'profile.html', context)


@login_required
def shop(request):
    try:
        player = Player.objects.get(user=request.user)
        shop = Shop.objects.get(player=player)
        items = shop.items.all()
    except (Player.DoesNotExist, Shop.DoesNotExist):
        shop = None
        items = None

    context = {
        'shop': shop,
        'items': items
    }
    return render(request, 'shop.html', context)


@login_required
def purchase_item(request, item_id):
    item = Item.objects.get(id=item_id)
    inventory = Inventory.objects.get(player__user=request.user)
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


@login_required
def inventory(request):
    try:
        inventory = Inventory.objects.get(player__user=request.user)
    except ObjectDoesNotExist:
        # Create a new inventory record for the user if it doesn't exist
        inventory = Inventory.objects.create(player=Player.objects.get(user=request.user))

    items = inventory.items.all()

    context = {
        'inventory': inventory,
        'items': items
    }

    return render(request, 'inventory.html', context)


@login_required
def settings(request):
    player = Player.objects.get(user=request.user)
    settings = Settings.objects.get(player=player)

    context = {
        'player': player,
        'settings': settings
    }

    return render(request, 'settings.html', context)