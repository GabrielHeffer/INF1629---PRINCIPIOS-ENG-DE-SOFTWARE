from django.urls import path
from .views import index, resultado

urlpatterns = [
    path('', index),
    path('resultado', resultado)
]