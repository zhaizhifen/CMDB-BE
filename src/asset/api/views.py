# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    )

from asset.models import ServerInfo, ServerStatus
from asset.serializers import (
    ServerInfoSerializer,
    ServerStatusSerializer,
    )


# for server info apiviews
class ServerInfoCreate(CreateAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class ServerInfoList(ListAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class ServerInfoRetrieve(RetrieveAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"


class ServerInfoUpdate(RetrieveUpdateAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"


class ServerInfoDelete(RetrieveDestroyAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"


# # for server status  apiviews
# class ServerStatusCreate(CreateAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerStatusSerializer
#
#
# class ServerStatusList(RetrieveAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerStatusSerializer
#
#
# class ServerStatusRetrieve(RetrieveAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerStatusSerializer
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
#
#
# class ServerStatusUpdate(RetrieveUpdateAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerStatusSerializer
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
#
#
# class ServerStatusDelete(RetrieveDestroyAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerStatusSerializer
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
