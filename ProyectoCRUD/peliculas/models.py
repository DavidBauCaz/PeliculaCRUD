from django.db import models

# modelos para pelicula

class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    descripcion = models.TextField()
    poster = models.CharField(max_length=500, blank=True, null=True, help_text='Ruta local del póster')
    actores_principales = models.TextField()
    fecha_salida = models.DateField()
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)
    idiomas = models.TextField()
    duracion = models.PositiveBigIntegerField(help_text='Duración en minutos')
    estrellas = models.IntegerField()
    
    def __str__(self):
        return self.titulo
