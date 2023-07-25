import subprocess

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Player, PlayerProfile, Item, Shop, Inventory, InventoryItem, Settings
from django.contrib.auth.decorators import login_required


def start_screen(request):
    return render(request, 'start_screen.html')


@login_required
def profile(request):
    try:
        player = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        player = None

    try:
        player_profile = PlayerProfile.objects.get(player=player)
        achievements = player_profile.achievements.all()
    except PlayerProfile.DoesNotExist:
        player_profile = None
        achievements = None

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
        'player': player,
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
        items = inventory.items.all()
    except ObjectDoesNotExist:
        # Check if Player exists before creating new Inventory
        try:
            player = Player.objects.get(user=request.user)
            inventory = Inventory.objects.create(player=player)
            items = inventory.items.all()
        except Player.DoesNotExist:
            player = None
            inventory = None
            items = None

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


def start_game(request):
    # Путь до файла игры
    start_the_game = 'tomatoes/models.py'

    # Запуск скрипта игры
    subprocess.run(f"python3 {start_the_game}", shell=True)

    return HttpResponse("Game started")
