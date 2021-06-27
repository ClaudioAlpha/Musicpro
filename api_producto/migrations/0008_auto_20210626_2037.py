# Generated by Django 3.2.3 on 2021-06-27 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_producto', '0007_auto_20210626_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='id_catalogo',
        ),
        migrations.AddField(
            model_name='historicalproductos',
            name='catalogo',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='api_producto.catalogo'),
        ),
        migrations.AddField(
            model_name='productos',
            name='catalogo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_producto.catalogo'),
            preserve_default=False,
        ),
    ]