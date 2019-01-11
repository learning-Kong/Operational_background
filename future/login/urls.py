# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django.urls import path

from . import views
urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
]
