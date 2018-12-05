from django.contrib import admin

# Register your models here.
from .models import User, Group, Memberships, Authorityinfo

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Memberships)
admin.site.register(Authorityinfo)