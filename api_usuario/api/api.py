from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api_usuario.models import Usuario
from api_usuario.api.serializers import UsuarioSerializer


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
