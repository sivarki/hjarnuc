# Generated by Django 2.1.1 on 2018-10-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0010_auto_20181008_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default='离线', max_length=64),
        ),
    ]
