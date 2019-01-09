from django.urls import path
from . import views


urlpatterns = [
    path('idc_list/', views.list),
]