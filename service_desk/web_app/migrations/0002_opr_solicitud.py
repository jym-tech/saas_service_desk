# Generated by Django 4.0.3 on 2022-04-11 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opr_Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_solicitud', models.CharField(max_length=50)),
                ('diagnostico_solicitud', models.CharField(max_length=500)),
                ('fecha_creacion_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion_solicitud', models.DateTimeField(auto_now=True)),
                ('fecha_baja_solicitud', models.DateTimeField()),
                ('fecha_estimada_entrega_solicitud', models.DateTimeField()),
                ('fecha_entrega_solicitud', models.DateTimeField()),
                ('activo_solicitud', models.BooleanField(default=True)),
                ('id_cliente_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idCliente', to='web_app.cat_cliente')),
                ('id_equipo_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idEquipo', to='web_app.cat_equipo')),
            ],
        ),
    ]