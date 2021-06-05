from rest_framework.response import Response
from rest_framework.views import APIView
from api_producto.models import Producto
from api_producto.api.serializers import ProductoSerializer

class ProductoAPIView(APIView):

    def get(self,request):
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos, many=True)
        return Response(productos_serializer.data)
