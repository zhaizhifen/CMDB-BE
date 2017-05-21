# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from asset import views


urlpatterns = [
    url(r'^api/server_info/$', views.server_info_list,
        name="server_info list&update"),
    url(r'^api/server_info/(?P<uuid>(.*))$', views.server_info_detail,
        name="server_info retrieve&update&delete"),
    url(r'^api/server_status/$', views.server_status_list,
        name="server_status list&update"),
    url(r'^api/server_status/(?P<uuid>(.*))$', views.server_status_detail,
        name="server_status retrieve&update&delete"),
]
