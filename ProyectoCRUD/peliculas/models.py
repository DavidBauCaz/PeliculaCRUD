from django.db import models

# modelo pelicula
# Vamos a utilizar la información que normalmente se muestra de las películas como en el cine y netflix. 

class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    descripcion = models.TextField()
    poster = models.CharField(max_length=500, blank=True, null=True, help_text='Ruta local del póster') # Aqui se debe p asar un link de imagen de internet para que funcione
    actores_principales = models.TextField()
    fecha_salida = models.DateField() # fecha de salida de la película, puede ser en formato dd-mm-aaaa o dd/mm/aaaa
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10)
    idiomas = models.TextField()
    duracion = models.PositiveBigIntegerField(help_text='Duración en minutos') # duración de la pelicula en minutos
    estrellas = models.IntegerField() # numero de 0 a 5 para la calificación de la pelicula
    
    def __str__(self):
        return self.titulo
