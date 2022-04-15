# Generated by Django 4.0.3 on 2022-04-15 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_app', '0005_alter_opr_solicitud_fecha_baja_solicitud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opr_solicitud',
            name='usuario_solicitud',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opr_solicitud',
            name='id_cliente_solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_solicitud', to='web_app.cat_cliente'),
        ),
        migrations.AlterField(
            model_name='opr_solicitud',
            name='id_equipo_solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_solicitud', to='web_app.cat_equipo'),
        ),
    ]