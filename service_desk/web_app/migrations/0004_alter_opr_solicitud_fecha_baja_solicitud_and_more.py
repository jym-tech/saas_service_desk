# Generated by Django 4.0.3 on 2022-04-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_alter_opr_solicitud_fecha_baja_solicitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opr_solicitud',
            name='fecha_baja_solicitud',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='opr_solicitud',
            name='fecha_entrega_solicitud',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='opr_solicitud',
            name='fecha_estimada_entrega_solicitud',
            field=models.DateField(default=None),
        ),
    ]
