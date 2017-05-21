# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from asset.models import ServerInfo, ServerStatus
from asset.serializers import ServerInfoSerializer, ServerStatusSerializer


@api_view(['GET'])
@csrf_exempt
def server_info_list(request):
    """
    List all code server_info, or create a new server_info.
    """
    if request.method == 'GET':
        server_info = ServerInfo.objects.all()
        serializer = ServerInfoSerializer(server_info, many=True)
        resData = {
            "code": 0,
            "message": "succeed",
            "data": serializer.data
        }
        return Response(resData)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@csrf_exempt
def server_info_detail(request, uuid):
    """
    Retrieve, update or delete a code server_info.
    """
    if request.method == 'GET':
        try:
            server_info = ServerInfo.objects.get(pk=uuid)
            serializer = ServerInfoSerializer(server_info)
            resData = {
                "code": 0,
                "message": "succeed",
                "data": serializer.data
            }
            return Response(resData)
        except ServerInfo.DoesNotExist:
            resData = {
                "code": 1,
                "message": "{0} is not found.".format(uuid)
            }
            return Response(resData)

    elif request.method == 'PUT':
        serializer = ServerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resData = {
                "code": 0,
                "message": "succeed"
            }
            return Response(resData)
        else:
            resData = {
                "code": 1,
                "message": serializer.errors
            }
            return Response(resData)

    elif request.method == 'POST':
        try:
            server_info = ServerInfo.objects.get(pk=uuid)
            serializer = ServerInfoSerializer(server_info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                resData = {
                    "code": 0,
                    "message": "succeed"
                }
                return Response(resData)
            else:
                resData = {
                    "code": 1,
                    "message": serializer.errors
                }
                return Response(resData)
        except ServerInfo.DoesNotExist:
            resData = {
                "code": 1,
                "message": "{0} is not found.".format(uuid)
            }
            return Response(resData)

    elif request.method == 'DELETE':
        try:
            server_info = ServerInfo.objects.get(pk=uuid)
            server_info.delete()
            resData = {
                "code": 0,
                "message": "succeed"
            }
            return Response(resData)
        except ServerInfo.DoesNotExist:
            resData = {
                "code": 1,
                "message": "{0} is not found.".format(uuid)
            }
            return Response(resData)


@api_view(['GET'])
@csrf_exempt
def server_status_list(request):
    """
    List all code server_status, or create a new server_status.
    """
    if request.method == 'GET':
        server_status = ServerStatus.objects.all()
        serializer = ServerStatusSerializer(server_status, many=True)
        resData = {
            "code": 0,
            "message": "succeed",
            "data": serializer.data
        }
        return Response(resData)


@api_view(['GET', 'POST'])
@csrf_exempt
def server_status_detail(request, uuid):
    """
    Retrieve, update or delete a code server_status.
    """
    if request.method == 'GET':
        try:
            server_status = ServerStatus.objects.get(pk=uuid)
            print server_status
            serializer = ServerStatusSerializer(server_status)
            resData = {
                "code": 0,
                "message": "succeed",
                "data": serializer.data
            }
            return Response(resData)
        except ServerStatus.DoesNotExist:
            resData = {
                "code": 1,
                "message": "{0} is not found.".format(uuid)
            }
            return Response(resData)

    elif request.method == 'POST':
        try:
            server_status = ServerStatus.objects.get(pk=uuid)
            serializer = ServerStatusSerializer(server_status, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                resData = {
                    "code": 0,
                    "message": "succeed"
                }
                return Response(resData)
            else:
                resData = {
                    "code": 1,
                    "message": serializer.errors
                }
                return Response(resData)
        except ServerStatus.DoesNotExist:
            resData = {
                "code": 1,
                "message": "{0} is not found.".format(uuid)
            }
            return Response(resData)
