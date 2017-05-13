# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from asset import views

urlpatterns = [
    url(r'^asset/server_info/$', views.server_info_list),
    url(r'^asset/server_info/(?P<pk>[0-9]+)/$', views.server_info_detail),
    url(r'^asset/server_status/$', views.server_status_list),
    url(r'^asset/server_status/(?P<pk>[0-9]+)/$', views.server_status_detail),
]
