# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from asset.models import ServerInfo, ServerStatus
from asset.serializers import ServerInfoSerializer, ServerStatusSerializer


@csrf_exempt
def server_info_list(request):
    """
    List all code server_info, or create a new server_info.
    """
    if request.method == 'GET':
        server_info = ServerInfo.objects.all()
        serializer = ServerInfoSerializer(server_info, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServerInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def server_status_list(request):
    """
    List all code server_status, or create a new server_status.
    """
    if request.method == 'GET':
        server_status = ServerStatus.objects.all()
        serializer = ServerStatusSerializer(server_info, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServerStatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def server_info_detail(request, pk):
    """
    Retrieve, update or delete a code server_info.
    """
    try:
        server_info = ServerInfo.objects.get(pk=pk)
    except ServerInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServerInfoSerializer(server_info)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerInfoSerializer(server_info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        server_info.delete()
        return HttpResponse(status=204)


@csrf_exempt
def server_status_detail(request, pk):
    """
    Retrieve, update or delete a code server_status.
    """
    try:
        server_status = ServerStatus.objects.get(pk=pk)
    except ServerStatus.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServerStatusSerializer(server_status)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerStatusSerializer(server_status, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        server_status.delete()
        return HttpResponse(status=204)
