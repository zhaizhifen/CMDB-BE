# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class ServerInfo(models.Model):
    HDD, SSD = range(0, 2)
    uuid = models.CharField(primary_key=True, max_length=37)
    manufactory = models.CharField('Manufactory', max_length=255)
    model = models.CharField('Models', max_length=255)
    cpu = models.SmallIntegerField('CPU')
    mem = models.SmallIntegerField('Memory')
    DISK_TYPE_CHOICES = (
        (HDD, 'HDD'),
        (SSD, 'SSD'),
    )
    disk_type = models.CharField(
            max_length=1,
            choices=DISK_TYPE_CHOICES,
            default=HDD,
    )
    disk_capacity = models.SmallIntegerField('Disk')
    nic = models.CharField('NIC', max_length=255, blank=True, null=True)
    idc = models.CharField('IDC', max_length=255, blank=True, null=True)
    apply_date = models.DateField('DateOfApplication')
    expire_date = models.DateField('DateOfExpire')

    def __str__(self):
        return self.uuid

    def __unicode__(self):
        return self.uuid

    class Meta:
        verbose_name = "server information"


class ServerStatus(models.Model):
    ALLOCATED, UNALLOCATED, RECYCLED = range(0, 3)
    NORMAL, ERROR, OUT_OF_WARRANTY = range(0, 3)
    server_info = models.OneToOneField(
        ServerInfo,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='server_status'
    )
    project = models.CharField('PROJECT', max_length=255)
    owner = models.CharField('PersonInCharge', max_length=255, blank=True, null=True)
    ALLOCATION_STATUS_CHOICES = (
        (ALLOCATED, 'allocated'),
        (UNALLOCATED, 'unallocated'),
        (RECYCLED, 'recycled'),
    )
    allocation_status = models.CharField(
        max_length=1,
        choices=ALLOCATION_STATUS_CHOICES,
        default=ALLOCATED,
    )
    HEALTH_STATUS_CHOICES = (
        (NORMAL, 'normal'),
        (ERROR, 'error'),
        (OUT_OF_WARRANTY, 'out_of_warranty'),
    )
    health_status = models.CharField(
        max_length=1,
        choices=HEALTH_STATUS_CHOICES,
        default=NORMAL,
    )

    def __str__(self):
        return self.server_info.uuid

    def __unicode__(self):
        return self.server_info.uuid

    class Meta:
        verbose_name = "server status"
