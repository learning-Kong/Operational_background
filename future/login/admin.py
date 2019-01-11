# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django.contrib import admin
from .models import UserGroup


# Register your models here.

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ("department", "position", "permission")
    list_per_page = 5
    ordering = ("-department", "permission", "position")

admin.site.register(UserGroup, UserGroupAdmin)
