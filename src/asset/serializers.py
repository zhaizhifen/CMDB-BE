# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from asset.models import ServerInfo, ServerStatus


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('__all__')


class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatus
        fields = ('__all__')

    def create(self, validated_data):
        server_uuid = validated_data.pop('server_info')
        try:
            server_info = ServerInfo.objects.get(uuid=server_uuid)
        except ServerInfo.DoesNotExist:
            raise ValidationError("No such server:%s" % server_uuid)
        server_status = ServerStatus.objects.create(server_info=server_info, **validated_data)
        return server_status

