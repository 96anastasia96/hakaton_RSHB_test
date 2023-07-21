from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

# отключаем стандартный UserAdmin
admin.site.unregister(User)


# создаем новый CustomUserAdmin на базе UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(PlayerProfile)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Achievement)

