from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('auth/', views.auth),
    path('checkout/', views.checkout),
    path('index/', views.index),
    path('test/', views.test),
    path('aa/', views.aa),
    path('login/', views.logins),
]