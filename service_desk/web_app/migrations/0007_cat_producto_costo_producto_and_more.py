# Generated by Django 4.0.3 on 2022-04-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_opr_solicitud_usuario_solicitud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_producto',
            name='costo_producto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='cat_servicio',
            name='costo_servicio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
