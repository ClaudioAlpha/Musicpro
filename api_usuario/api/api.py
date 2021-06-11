from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api_usuario.models import Usuario
from api_usuario.api.serializers import UsuarioSerializer
from django.views.generic import TemplateView, ListView


class UsuarioAPIView(APIView):

    def get(self,request):
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios,many=True)
        return Response(usuarios_serializer.data)


class Inicio(TemplateView):
    template_name = 'index.html'



#class ListadoUsuario(ListView):
#    template_name =


@api_view(['GET','PUT','DELETE'])
def detalle_usuario_api_view(request,pk=None):

    if request.method == 'GET':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)

    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario, data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario.delete()
        return Response('Usuario Eliminado Exitosamente!')








"""
@api_view(['GET','POST'])
def usuario_api_view(request):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return Response(usuarios_serializer.data)

    elif request.method == 'POST':
        usuario_serializer = UsuarioSerializer(data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def detalle_usuario_api_view(request,pk=None):

    if request.method == 'GET':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)

    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario, data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario.delete()
        return Response('Usuario Eliminado Exitosamente!')
"""
