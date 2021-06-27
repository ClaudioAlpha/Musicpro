from rest_framework import serializers
from api_producto.models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
