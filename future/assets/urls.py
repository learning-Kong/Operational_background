from django.urls import path
from . import views


urlpatterns = [
    path('idc_list/', views.idc_list),
    path('idc_add/', views.idc_add),
    path('idc_change/', views.idc_change),
    path('idc_del/', views.idc_del),
]
