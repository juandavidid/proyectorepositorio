# Generated by Django 4.0.4 on 2022-05-21 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio_venta',
            new_name='precio',
        ),
    ]
