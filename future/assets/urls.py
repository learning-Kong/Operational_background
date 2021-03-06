# -*- coding:utf-8 -*-
# author: "Xianglei Kong"


from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('idc_list/', views.idc_list),
    path('idc_add/', views.idc_add),
    path('idc_change/', views.idc_change),
    path('idc_del/', views.idc_del),
    path('project/add/', views.project_add),
    path('project/list/', views.project_list),
    path('project/change/', views.project_edit),
    path('project/del/', views.project_del),
    path('host/add/', views.host_add),
    path('host/list/', views.host_list),
    path('host/del_batch/', views.host_del_batch),
    path('host/change_info_ajax/', views.host_search),
    url(r'^host/edit/', views.host_edit),
    path('host/detail/', views.host_detail),
    path('host/del/', views.host_del),
    path('host/bak/', views.host_bak),
]
