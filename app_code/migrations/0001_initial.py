# Generated by Django 2.1.1 on 2018-12-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_name', models.CharField(max_length=64, unique=True)),
                ('git_msg', models.CharField(max_length=64, null=True)),
                ('git_url', models.CharField(max_length=128, unique=True)),
                ('git_user', models.CharField(max_length=64, null=True)),
                ('git_passwd', models.CharField(max_length=64, null=True)),
                ('git_sshkey', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=32, unique=True)),
                ('project_msg', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publist_dir', models.CharField(max_length=128)),
                ('publist_msg', models.CharField(max_length=128, null=True)),
                ('current_version', models.CharField(max_length=64, null=True)),
                ('version_info', models.CharField(max_length=512, null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('publist_date', models.CharField(max_length=64, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('gitcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_code.GitCode')),
                ('host_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_asset.Host')),
            ],
        ),
        migrations.CreateModel(
            name='PublistRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_version', models.CharField(max_length=64, null=True)),
                ('version_info', models.CharField(max_length=1024, null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('publist_date', models.CharField(max_length=64, null=True)),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('publist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_code.Publist')),
            ],
        ),
        migrations.CreateModel(
            name='Wchartlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=64, null=True)),
                ('from_user', models.CharField(max_length=64, null=True)),
                ('up_connect', models.CharField(max_length=2048, null=True)),
                ('up_id', models.CharField(max_length=64, null=True)),
                ('status', models.CharField(default='waiting', max_length=64)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gitcode',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_code.Project'),
        ),
    ]
