# Generated by Django 3.2.3 on 2021-06-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_producto', '0003_auto_20210626_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproducto',
            name='caract_producto',
            field=models.TextField(blank=True, null=True, verbose_name='Caracteristicas Producto'),
        ),
        migrations.AlterField(
            model_name='historicalproducto',
            name='marca_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca Producto'),
        ),
        migrations.AlterField(
            model_name='historicalproducto',
            name='modelo_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo Producto'),
        ),
        migrations.AlterField(
            model_name='historicalproducto',
            name='nombre_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='caract_producto',
            field=models.TextField(blank=True, null=True, verbose_name='Caracteristicas Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='modelo_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Producto'),
        ),
    ]
