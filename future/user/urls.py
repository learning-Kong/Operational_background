from django.urls import path

from . import views
urlpatterns = [
    path('add/', views.add),
    path('change/', views.change),
]