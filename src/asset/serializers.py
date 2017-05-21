# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from asset.models import ServerInfo, ServerStatus


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('__all__')

    def create(self, validated_data):
        server_uuid = validated_data.pop('uuid')
        server_info = ServerInfo.objects.create(uuid=server_uuid, **validated_data)
        server_info_id = ServerInfo.objects.get(uuid=server_uuid)
        server_status = ServerStatus.objects.create(server_info=server_info_id)
        return server_info, server_status


class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatus
        fields = ('__all__')
