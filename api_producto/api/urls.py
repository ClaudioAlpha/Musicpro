from django.urls import path
from .api import ProductoAPIView

urlpatterns = [
    path('producto/',ProductoAPIView.as_view(), name='producto_api')

    ]
