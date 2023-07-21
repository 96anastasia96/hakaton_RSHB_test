from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    wallet = models.IntegerField(default=0)
    bank_balance = models.IntegerField(default=0)
    credit_limit = models.IntegerField(default=0)
    credit_balance = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.user.username

    def can_afford_item(self, item):
        return self.wallet + self.bank_balance + self.credit_balance >= item.price


class PlayerProfile(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    achievements = models.ManyToManyField('Achievement')

    def __str__(self):
        return f"{self.player.username}'s Profile"


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Shop(models.Model):
    items = models.ManyToManyField(Item)
    player = models.OneToOneField(Player, on_delete=models.CASCADE)



class Inventory(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='InventoryItem')

    def __str__(self):
        return f"{self.player.username}'s Inventory"


class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} ({self.inventory.player.username})"


class Settings(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    sound_enabled = models.BooleanField(default=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.player.username}'s Settings"


