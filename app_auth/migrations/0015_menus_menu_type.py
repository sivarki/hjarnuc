# Generated by Django 2.1.1 on 2018-10-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0014_auto_20181008_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='menu_type',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]