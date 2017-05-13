# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from asset import views

# api test
from asset.api import views as api_views

urlpatterns = [
    url(r'^asset/server_info/$', views.server_info_list,
        name="server_info list&update"),
    url(r'^asset/server_info/(?P<pk>[0-9]+)/$', views.server_info_detail,
        name="server_info retrieve&update&delete"),
    url(r'^asset/server_status/$', views.server_status_list,
        name="server_status list&update"),
    url(r'^asset/server_status/(?P<pk>[0-9]+)/$', views.server_status_detail,
        name="server_status retrieve&update&delete"),

    # api test views
    url(r'^asset/api/server_info/create/$',
        api_views.ServerInfoCreate.as_view(),
        name="server_info apitest create"),
    url(r'^asset/api/server_info/$',
        api_views.ServerInfoList.as_view(),
        name="server_info apitest list"),
    url(r'^asset/api/server_info/(?P<uuid>[0-9]+)/$',
        api_views.ServerInfoRetrieve.as_view(),
        name="server_info apitest retrieve"),
    url(r'^asset/api/server_info/(?P<uuid>[0-9]+)/edit/$',
        api_views.ServerInfoUpdate.as_view(),
        name="server_info apitest update"),
    url(r'^asset/api/server_info/(?P<uuid>[0-9]+)/delete/$',
        api_views.ServerInfoDelete.as_view(),
        name="server_info apitest delete"),

    url(r'^asset/api/server_status/create/$',
        api_views.ServerStatusCreate.as_view(),
        name="server_status apitest create"),
    url(r'^asset/api/server_status/$',
        api_views.ServerStatusList.as_view(),
        name="server_status apitest list"),
    url(r'^asset/api/server_status/(?P<uuid>[0-9]+)/$',
        api_views.ServerStatusRetrieve.as_view(),
        name="server_status apitest retrieve"),
    url(r'^asset/api/server_status/(?P<uuid>[0-9]+)/edit/$',
        api_views.ServerStatusUpdate.as_view(),
        name="server_status apitest update"),
    url(r'^asset/api/server_status/(?P<uuid>[0-9]+)/delete/$',
        api_views.ServerStatusDelete.as_view(),
        name="server_status apitest delete"),
]
