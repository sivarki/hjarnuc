# Generated by Django 2.1.1 on 2018-10-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0011_auto_20181026_1054'),
        ('app_log', '0005_taskrecord_task_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskrecord',
            name='task_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_auth.User'),
            preserve_default=False,
        ),
    ]
