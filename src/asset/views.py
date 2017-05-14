# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from asset.models import ServerInfo, ServerStatus
from asset.serializers import ServerInfoSerializer, ServerStatusSerializer


@api_view(['GET', 'POST'])
@csrf_exempt
def server_info_list(request):
    """
    List all code server_info, or create a new server_info.
    """
    if request.method == 'GET':
        server_info = ServerInfo.objects.all()
        serializer = ServerInfoSerializer(server_info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
def server_status_list(request):
    """
    List all code server_status, or create a new server_status.
    """
    if request.method == 'GET':
        server_status = ServerStatus.objects.all()
        serializer = ServerStatusSerializer(server_status, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServerStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def server_info_detail(request, server_id):
    """
    Retrieve, update or delete a code server_info.
    """
    try:
        server_info = ServerInfo.objects.get(pk=server_id)
    except ServerInfo.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = ServerInfoSerializer(server_info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServerInfoSerializer(server_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        server_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def server_status_detail(request, server_id):
    """
    Retrieve, update or delete a code server_status.
    """
    try:
        server_status = ServerStatus.objects.get(pk=server_id)
    except ServerStatus.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = ServerStatusSerializer(server_status)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServerStatusSerializer(server_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        server_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
