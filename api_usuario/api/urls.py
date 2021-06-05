from django.urls import path
from .api import usuario_api_view, detalle_usuario_api_view

urlpatterns = [
    path('usuario/',usuario_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', detalle_usuario_api_view, name= 'detalle_usuario_api_view')

    ]
