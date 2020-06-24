from django.urls import path
from .views import index, info

urlpatterns = [
    path('', index),
    path('info', info)
]