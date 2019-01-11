# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django.contrib import admin
from .models import IDC, Project
# Register your models here.

class IDCAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "operator", "type", "comment")

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "aliases_name", "business_name", "business_aliases_name", "use_name", "comment")

admin.site.register(IDC, IDCAdmin)
admin.site.register(Project, ProjectAdmin)
# admin.site.register(Project)

