# Generated by Django 2.1.1 on 2018-10-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0009_auto_20181008_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
