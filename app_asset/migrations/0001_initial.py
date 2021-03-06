# Generated by Django 2.1.1 on 2018-12-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=64, unique=True)),
                ('host_remove_port', models.CharField(max_length=64, null=True)),
                ('host_user', models.CharField(max_length=128)),
                ('host_passwd', models.CharField(max_length=256)),
                ('host_type', models.CharField(max_length=64)),
                ('host_msg', models.CharField(max_length=256)),
                ('serial_num', models.CharField(max_length=256, null=True)),
                ('purchase_date', models.CharField(max_length=128, null=True)),
                ('overdue_date', models.CharField(max_length=128, null=True)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=128, null=True)),
                ('mem_size', models.CharField(max_length=128, null=True)),
                ('swap_size', models.CharField(max_length=64, null=True)),
                ('cpu_model', models.CharField(max_length=128, null=True)),
                ('cpu_nums', models.CharField(max_length=128, null=True)),
                ('disk_info', models.TextField(null=True)),
                ('interface', models.TextField(null=True)),
                ('os_type', models.CharField(max_length=128, null=True)),
                ('kernel_version', models.CharField(max_length=128, null=True)),
                ('os_version', models.CharField(max_length=128, null=True)),
                ('product_name', models.CharField(max_length=128, null=True)),
                ('host_status', models.CharField(max_length=32, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_asset.Host')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_group_name', models.CharField(max_length=64, unique=True)),
                ('host_group_msg', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc_name', models.CharField(max_length=64, unique=True)),
                ('idc_msg', models.CharField(max_length=128, null=True)),
                ('idc_admin', models.CharField(max_length=128, null=True)),
                ('idc_admin_phone', models.CharField(max_length=128, null=True)),
                ('idc_admin_email', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Netwk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netwk_ip', models.CharField(max_length=64, unique=True)),
                ('netwk_remove_port', models.CharField(max_length=64, null=True)),
                ('netwk_user', models.CharField(max_length=128)),
                ('netwk_passwd', models.CharField(max_length=256)),
                ('netwk_type', models.CharField(max_length=64)),
                ('netwk_msg', models.CharField(max_length=256)),
                ('serial_num', models.CharField(max_length=256, null=True)),
                ('purchase_date', models.CharField(max_length=128, null=True)),
                ('overdue_date', models.CharField(max_length=128, null=True)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.HostGroup')),
                ('idc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.IDC')),
            ],
        ),
        migrations.CreateModel(
            name='software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=256)),
                ('server_version', models.CharField(max_length=512, null=True)),
                ('server_port', models.CharField(max_length=1026, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_asset.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=128, unique=True)),
                ('supplier_head', models.CharField(max_length=128, null=True)),
                ('supplier_head_phone', models.CharField(max_length=128, null=True)),
                ('supplier_head_email', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='netwk',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.Supplier'),
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.HostGroup'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.IDC'),
        ),
        migrations.AddField(
            model_name='host',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_asset.Supplier'),
        ),
    ]
