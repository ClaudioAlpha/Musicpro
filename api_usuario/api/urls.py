from django.urls import path
from .api import Inicio, UsuarioAPIView, detalle_usuario_api_view

urlpatterns = [
    path('usuario/',UsuarioAPIView.as_view(), name='usuario_api'),
    path('usuario/<int:pk>/', detalle_usuario_api_view, name= 'detalle_usuario_api_view')

    ]
