# Generated by Django 3.2.3 on 2021-06-26 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_boleta', '0002_auto_20210626_1906'),
        ('api_producto', '0006_historicalproductos_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_catalogo',
        ),
        migrations.AlterModelOptions(
            name='historicalproductos',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Productos'},
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['SKU'], 'verbose_name': 'Productos', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelTable(
            name='productos',
            table='Productos',
        ),
        migrations.DeleteModel(
            name='HistoricalProducto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
