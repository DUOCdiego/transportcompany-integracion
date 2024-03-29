# Generated by Django 4.2.3 on 2024-01-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudTransporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_seguimiento', models.CharField(max_length=20, unique=True)),
                ('persona_origen', models.CharField(max_length=100)),
                ('direccion_origen', models.CharField(max_length=255)),
                ('persona_destino', models.CharField(max_length=100)),
                ('direccion_destino', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
            ],
        ),
    ]
