# Generated by Django 5.1.7 on 2025-03-28 19:08

import cloudinary.models
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AÑO', models.IntegerField(editable=False)),
                ('FECHA', models.DateField()),
                ('DIA', models.CharField(editable=False, max_length=20)),
                ('HORA', models.TimeField(blank=True, null=True)),
                ('CONTROLES_DE_TRANSITO', models.CharField(blank=True, max_length=255, null=True)),
                ('CLASE_DE_ACCIDENTE', models.CharField(max_length=100)),
                ('CLASE_DE_SERVICIO', models.CharField(max_length=100)),
                ('GRAVEDAD_DEL_ACCIDENTE', models.CharField(max_length=100)),
                ('CLASE_DE_VEHICULO', models.CharField(max_length=100)),
                ('AREA', models.CharField(blank=True, max_length=255, null=True)),
                ('DIRECCION_HECHO', models.CharField(blank=True, max_length=255, null=True)),
                ('BARRIO_HECHO', models.CharField(blank=True, max_length=255, null=True)),
                ('coordenada_geografica', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('imagen', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('confirmado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Aprobaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aprobacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
