from django.urls import path
from . import views


urlpatterns = [
    path('idc_list/', views.idc_list),
    path('idc_add/', views.idc_add),
]