# Generated by Django 3.1.3 on 2020-12-08 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_auto_20201129_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclubuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myclubuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myclubuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='volunteer',
            field=models.BooleanField(default=False),
        ),
    ]
