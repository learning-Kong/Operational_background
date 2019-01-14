from django.urls import path
from . import views

app_name = 'display'
urlpatterns = [
    path('index/', views.index),
    path('login/',views.login),
    path('chart/',views.chartdisplay),
    path('charttest/',views.chartss),
]