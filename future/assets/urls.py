from django.urls import path
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
]
