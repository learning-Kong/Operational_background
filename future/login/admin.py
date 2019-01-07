from django.contrib import admin
from .models import UserGroup


# Register your models here.

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ("department", "position", "permission")
    list_per_page = 4
    ordering = ("-department", "permission", "position")

admin.site.register(UserGroup, UserGroupAdmin)
