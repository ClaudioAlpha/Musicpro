from django.db import models
import datetime
from simple_history.models import HistoricalRecords
from api_producto.models import *

# Create your models here.


class ComprobanteCompra(models.Model):

    numero_pedido = models.IntegerField('Numero Pedido', primary_key=True, unique=True)
    fecha_pago = models.DateTimeField('Fecha Boleta', null=False)
    url_pagina_web = models.CharField('URL Pagina Web', max_length=300)
    codigo_autorizacion = models.IntegerField('Codigo de Autorizacion',blank=False, null=False)
    tipo_transaccion = models.CharField('Tipo Transaccion', max_length=50, null=False)
    numero_tarjeta = models.CharField('Estado de Pago Boleta', max_length=16, null=False)
    tipo_pago = models.CharField('Tipo de Pago', max_length=25, null=False)
    tipo_cuotas = models.CharField('Tipo de Cuotas', max_length=25, null=False)
    cantidad_cuotas = models.CharField('Cantidad de Cuotas', max_length=25, null=False)
    monto_total_pesos = models.IntegerField('Monto Total',blank=False, null=False)
    historico = HistoricalRecords()

    class Meta:
        ordering = ['numero_pedido']

    def __str__(self):
        return '{}/{}/{}/{}/{}/{}/{}/{}/{}/{}'.format(
            self.numero_pedido,
            self.fecha_pago,
            self.url_pagina_web,
            self.codigo_autorizacion,
            self.tipo_transaccion,
            self.numero_tarjeta,
            self.tipo_pago,
            self.tipo_cuotas,
            self.cantidad_cuotas,
            self.monto_total_pesos)


class Ventas(models.Model):

    numero_venta = models.IntegerField('Numero Pedido', primary_key=True, unique=True)
    fecha_registro = models.DateTimeField('Fecha Boleta', auto_now_add=True, null=False)
    numero_pedido = models.ForeignKey(ComprobanteCompra, on_delete=models.CASCADE)
    sku = models.ForeignKey(Productos, on_delete=models.CASCADE)
    historico = HistoricalRecords()

    class Meta:
        ordering = ['numero_venta']

    def __str__(self):
        return '{}/{}/{}/{}'.format(
            self.numero_venta,
            self.fecha_registro,
            self.numero_pedido,
            self.sku)
