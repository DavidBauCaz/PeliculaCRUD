# Generated by Django 5.1.5 on 2025-01-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('director', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('poster', models.CharField(blank=True, help_text='Ruta local del póster', max_length=500, null=True)),
                ('actores_principales', models.TextField()),
                ('fecha_salida', models.DateField()),
                ('genero', models.CharField(max_length=50)),
                ('clasificacion', models.CharField(max_length=10)),
                ('idiomas', models.TextField()),
                ('duracion', models.PositiveBigIntegerField(help_text='Duración en minutos')),
                ('estrellas', models.IntegerField()),
            ],
        ),
    ]
