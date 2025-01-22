from django.db import models

# modelos para pelicula

class pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    descripcion = models.TextField()
    actores_principales = models.TextField()
    fecha_salida = models.DateField()
    genero = models.CharField(max_length=50)
    idiomas = models.TextField()
    duracion = models.PositiveBigIntegerField(help_text='Duración en minutos')
    estrellas = models.IntegerField()
    
    def __str__(self):
        return self.titulo
