# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from asset.models import ServerInfo, ServerStatus


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('__all__')


class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatus
        fields = ('__all__')
