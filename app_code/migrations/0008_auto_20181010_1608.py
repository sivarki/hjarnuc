# Generated by Django 2.1.1 on 2018-10-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_code', '0007_auto_20181010_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitcode',
            name='git_passwd',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='gitcode',
            name='git_sshkey',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='gitcode',
            name='git_user',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
