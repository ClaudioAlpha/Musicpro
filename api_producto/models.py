from django.db import models
from simple_history.models import HistoricalRecords





class Productos(models.Model):

    SKU = models.IntegerField('sku', primary_key=True, blank=False, unique=True)
    NombreProducto = models.CharField('Nombre Producto', max_length=50, blank=False, null=True, help_text='aqui va el nombre')
    ModeloProducto = models.CharField('Modelo Producto', max_length=50, blank=False, null=True)
    MarcaProducto = models.CharField('Marca Producto', max_length=50, blank=False, null=True)
    Descripcion = models.TextField('Descripcion Producto', max_length=300, blank=False, null=True)


    CATALOGO_CHOICES = (
                ('Guitarras Acusticas','Guitarras Acusticas'),
                ('Guitarras Electricas','Guitarras Electricas'),
                ('Bajos Cuatro Cuerdas', 'Bajos Cuatro Cuerdas'),
                ('Bajos Cinco Cuerdas', 'Bajos Cinco Cuerdas'),
                ('Bajos Activos', 'Bajos Activos'),
                ('Bajos Pasivos', 'Bajos Pasivos'),
                ('Piano Media Cola', 'Piano Media Cola'),
                ('PianoCola Entera','PianoCola Entera'),
                ('Pianolas','Pianolas'),
                ('Baterias Acusticas','Baterias Acusticas'),
                ('Baterias Electricas','Baterias Electricas'),
                ('Pianolas','Pianolas'),
                ('Cabezales','Cabezales'),
                ('Cajas','Cajas'),
                )
    Catalogo = models.CharField(max_length=60, choices=CATALOGO_CHOICES, default=None, blank=False, null=True)
    imagen = models.FileField('Imagen de Producto', upload_to='Imagen_Producto/', blank=True, null=True)
    StockProducto = models.CharField('Stock Producto', max_length=50, blank=False, null=True)
    ValorProducto = models.IntegerField('Valor Producto',blank=False, null=False)
    historico = HistoricalRecords()

    class Meta:
        db_table = 'Productos'
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
        ordering = ['SKU']

    def __str__(self):
        return '{}/{}/{}/{}/{}/{}/{}/{}/{}' .format(self.SKU, self.NombreProducto, self.ModeloProducto, self.MarcaProducto, self.Descripcion, self.Catalogo, self.imagen, self.StockProducto, self.ValorProducto)
