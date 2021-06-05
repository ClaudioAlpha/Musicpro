from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api_producto.models import Producto
from api_producto.api.serializers import ProductoSerializer

@api_view(['GET','POST'])
def producto_api_view(request):

    if request.method == 'GET':
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos, many=True)
        return Response(productos_serializer.data)

    elif request.method == 'POST':
        producto_serializer = ProductoSerializer(data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)
