from django.urls import path

from . import views
urlpatterns = [
    path('add/', views.add),
    path('change/', views.change),
    path('change_userinfo/', views.change_userinfo),
]
