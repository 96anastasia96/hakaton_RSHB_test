# Generated by Django 4.2.3 on 2023-07-21 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.IntegerField(default=0)),
                ('bank_balance', models.IntegerField(default=0)),
                ('credit_limit', models.IntegerField(default=0)),
                ('credit_balance', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='main_screen.item')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_screen.player')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound_enabled', models.BooleanField(default=True)),
                ('language', models.CharField(max_length=50)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_screen.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('experience', models.IntegerField(default=0)),
                ('achievements', models.ManyToManyField(to='main_screen.achievement')),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_screen.player')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_screen.inventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_screen.item')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(through='main_screen.InventoryItem', to='main_screen.item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_screen.player'),
        ),
    ]
