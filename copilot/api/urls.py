
from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.get_current_time),
    path('hello/', views.get_hello),
    path('vms/', views.get_vms),
]
