from django.urls import path
from .api import producto_api_view, detalle_producto_api_view

urlpatterns = [
    path('productos/',producto_api_view, name='producto_api'),
    path('productos/<int:pk>/', detalle_producto_api_view, name ='detalle_producto_api_view')

    ]
