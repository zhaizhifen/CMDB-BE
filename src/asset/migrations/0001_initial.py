# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('uuid', models.CharField(max_length=37, primary_key=True, serialize=False)),
                ('manufactory', models.CharField(max_length=255, verbose_name='Manufactory')),
                ('model', models.CharField(max_length=255, verbose_name='Models')),
                ('cpu', models.SmallIntegerField(verbose_name='CPU')),
                ('mem', models.SmallIntegerField(verbose_name='Memory')),
                ('disk_type', models.CharField(choices=[(0, 'HDD'), (1, 'SSD')], default=0, max_length=1)),
                ('disk_capacity', models.SmallIntegerField(verbose_name='Disk')),
                ('nic', models.CharField(blank=True, max_length=255, null=True, verbose_name='NIC')),
                ('idc', models.CharField(blank=True, max_length=255, null=True, verbose_name='IDC')),
                ('apply_date', models.DateField(verbose_name='DateOfApplication')),
                ('expire_date', models.DateField(verbose_name='DateOfExpire')),
            ],
            options={
                'verbose_name': 'server information',
            },
        ),
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('server_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='server_status', serialize=False, to='asset.ServerInfo')),
                ('project', models.CharField(max_length=255, verbose_name='PROJECT')),
                ('owner', models.CharField(blank=True, max_length=255, null=True, verbose_name='PersonInCharge')),
                ('allocation_status', models.CharField(choices=[(0, 'allocated'), (1, 'unallocated'), (2, 'recycled')], default=0, max_length=1)),
                ('health_status', models.CharField(choices=[(0, 'normal'), (1, 'error'), (2, 'out_of_warranty')], default=0, max_length=1)),
            ],
            options={
                'verbose_name': 'server status',
            },
        ),
    ]