from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

admin.site.unregister(User)

admin.site.register(User)
admin.site.register(Player)
admin.site.register(PlayerProfile)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Achievement)

