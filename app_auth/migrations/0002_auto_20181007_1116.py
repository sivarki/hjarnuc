# Generated by Django 2.1.1 on 2018-10-07 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menus',
            name='menus_perms',
        ),
        migrations.AddField(
            model_name='menus',
            name='menus_perms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_auth.Perms'),
        ),
    ]