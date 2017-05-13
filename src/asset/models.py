# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class ServerInfo(models.Model):
    uuid = models.CharField(primary_key=True, max_length=37)
    manufactory = models.CharField('Manufactory', max_length=255)
    model = models.CharField('Models', max_length=255)
    cpu = models.SmallIntegerField('CPU')
    mem = models.SmallIntegerField('Memory')
    DISK_TYPE_CHOICES = (
        (0, 'HDD'),
        (1, 'SSD'),
    )
    disk_type = models.CharField(
            max_length=1,
            choices=DISK_TYPE_CHOICES,
            default=0,
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
    uuid = models.OneToOneField(
        ServerInfo,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='uuid_name'
    )
    project = models.CharField('PROJECT', max_length=255)
    pic = models.CharField('PersonInCharge', max_length=255, blank=True, null=True)
    ALLOCATION_STATUS_CHOICES = (
        (0, 'allocated'),
        (1, 'unallocated'),
        (2, 'recycled'),
    )
    allocation_status = models.CharField(
        max_length=1,
        choices=ALLOCATION_STATUS_CHOICES,
        default=0,
    )
    HEALTH_STATUS_CHOICES = (
        (0, 'normal'),
        (1, 'error'),
        (2, 'out_of_warranty'),
    )
    health_status = models.CharField(
        max_length=1,
        choices=HEALTH_STATUS_CHOICES,
        default=0,
    )

    def __str__(self):
        return self.uuid

    def __unicode__(self):
        return self.uuid

    class Meta:
        verbose_name = "server status"
