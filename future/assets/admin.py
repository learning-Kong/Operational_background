from django.contrib import admin
from .models import IDC
# Register your models here.

class IDCAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "operator", "type", "comment")

admin.site.register(IDC, IDCAdmin)
