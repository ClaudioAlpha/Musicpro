from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.


class Producto(models.Model):
    sku = models.IntegerField('SKU', primary_key=True, unique=True)
    nombre_producto = models.CharField('Nombre Producto', max_length=50, blank=False, null=False)
    modelo_producto = models.CharField('Modelo Producto', max_length=50, blank=False, null=False)
    marca_producto = models.CharField('Marca Producto', max_length=50, blank=False, null=False)
    caract_producto = models.TextField('Caracteristicas Producto', blank=False, null=False)
    catalogo_producto = models.CharField('Catalogo Producto', max_length=50, blank=False, null=False)
    imagen = models.ImageField('Imagen de Producto', upload_to='Imagen_Producto/', blank=True, null=True)
    precio_producto = models.IntegerField('Precio Producto',blank=False, null=False)
    historico = HistoricalRecords()


    def __str__(self):
        return '{}/{}/{}/{}/{}/{}'.format(
            self.sku,
            self.nombre_producto,
            self.modelo_producto,
            self.marca_producto,
            self.catalogo_producto,
            self.imagen)
