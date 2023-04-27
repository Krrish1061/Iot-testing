from django.urls import path
from . import views

# from .signals import *

# URLConfig
urlpatterns = [
    path("", views.home),
    path("api/sensor-value/", views.sensor_value_list),
]
