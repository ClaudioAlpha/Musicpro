from django.urls import path
from .api import producto_api_view

urlpatterns = [
    path('producto/',producto_api_view, name='producto_api')

    ]
