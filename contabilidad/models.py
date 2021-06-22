from django.db import models
from simple_history.models import HistoricalRecords
from api_producto.models import Producto

# Create your models here.

class VentasBoleta(models.Model):
    numero_boleta = models.IntegerField('Numero Boleta', primary_key=True, unique=True,auto_created=True)
    fecha_boleta = models.DateTimeField('Fecha Boleta', auto_now_add=True)
    detalle_boleta = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estado_pago_boleta = models.CharField('Estado de Pago Boleta', max_length=2)
    monto_boleta = models.IntegerField('Valor Total')
    historico = HistoricalRecords()

    class Meta:
        ordering = ['numero_boleta']

    def __str__(self):
        return '{}/{}/{}/{}/{}'.format(
            self.numero_boleta,
            self.fecha_boleta,
            self.detalle_boleta,
            self.estado_pago_boleta,
            self.monto_boleta)



class VentasFactura(models.Model):
    numero_factura = models.IntegerField('Numero Factura', primary_key=True, unique=True, auto_created=True)
    fecha_factura = models.DateTimeField('Fecha Factura', auto_now_add=True)
    detalle_factura = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estado_pago_factura = models.CharField('Estado de Pago Factura', max_length=2)
    monto_neto = models.IntegerField('Valor Neto')
    monto_iva = models.FloatField('IVA')
    monto_total = models.IntegerField('Valor Total')
    historico = HistoricalRecords()


    class Meta:
        ordering = ['numero_factura']

    def __str__(self):
        return '{}/{}/{}/{}/{}/{}/{}'.format(
            self.numero_factura,
            self.fecha_factura,
            self.detalle_factura,
            self.estado_pago_factura,
            self.monto_neto,
            self.monto_iva,
            self.monto_total)
