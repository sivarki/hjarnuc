# Generated by Django 2.1.1 on 2018-10-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0011_auto_20181008_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='menus_order',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
