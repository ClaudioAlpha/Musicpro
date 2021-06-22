from django.db import models
from simple_history.models import HistoricalRecords


# Categorias de productos.
class Catalogo(models.Model):
    nombre_catalogo = models.CharField(max_length=50)
    feature = models.BooleanField(default=False)
    historico = HistoricalRecords()
    def __str__(self):
        return self.nombre_catalogo

    class Meta:
        db_table = 'catalogo'
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ['nombre_catalogo']



# Stock de productos.
class StockProducto(models.Model):
    cantidad = models.IntegerField()
    historico = HistoricalRecords()
    def __str__(self):
        return self.nombre_catalogo

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock Productos'
        ordering = ['id']

# definir opciones del catalogo

class Producto(models.Model):

    sku = models.IntegerField('SKU', primary_key=True, unique=True)
    nombre_producto = models.CharField('Nombre Producto', max_length=50, blank=False, null=False)
    modelo_producto = models.CharField('Modelo Producto', max_length=50, blank=False, null=False)
    marca_producto = models.CharField('Marca Producto', max_length=50, blank=False, null=False)
    caract_producto = models.TextField('Caracteristicas Producto', blank=False, null=False)
    catalogo_producto = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    imagen = models.FileField('Imagen de Producto', upload_to='Imagen_Producto/', blank=True, null=True)
    precio_producto = models.IntegerField('Precio Producto',blank=False, null=False)
    historico = HistoricalRecords()

    class Meta:
        ordering = ['catalogo_producto','nombre_producto']


    def __str__(self):
        return '{}/{}/{}/{}/{}/{}'.format(
            self.sku,
            self.nombre_producto,
            self.modelo_producto,
            self.marca_producto,
            self.catalogo_producto,
            self.imagen)
