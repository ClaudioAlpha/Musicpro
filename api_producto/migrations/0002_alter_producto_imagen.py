# Generated by Django 3.2.3 on 2021-06-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Imagen_Producto/', verbose_name='Imagen de Producto'),
        ),
    ]
