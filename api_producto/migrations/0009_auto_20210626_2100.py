# Generated by Django 3.2.3 on 2021-06-27 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_producto', '0008_auto_20210626_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalproductos',
            old_name='catalogo',
            new_name='Catalogo',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='catalogo',
            new_name='Catalogo',
        ),
    ]