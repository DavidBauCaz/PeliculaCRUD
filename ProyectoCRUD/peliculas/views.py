from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pelicula
from django.urls import reverse_lazy

#vista para mostrar las películas
class ListarPeliculas(ListView):
    model = Pelicula # Modelo al que vamos a acceder en el template
    template_name = "peliculas/read.html" # template que se va a renderizar para mostrar la lista de los datos
    context_object_name = "peliculas"  # contexto que le vamos a pasar al template como variable llamada 'peliculas' y con el que accedemos a los datos de la base
    
#vista para ver más acerca de la película
class DetallesPelicula(DetailView):
    model = Pelicula
    template_name = 'peliculas/detalles.html'
    context_object_name = 'pelicula'
    
class CrearPelicula(CreateView):
    model = Pelicula
    template_name = 'peliculas/create.html'
    fields = ['titulo', 'director', 'descripcion', 'poster', 'actores_principales', 'fecha_salida', 'genero', 'clasificacion', 'idiomas',
              'duracion', 'estrellas']
    success_url = reverse_lazy('listar-peliculas') # url al que vamos a redirigir al usuario cuando termine de agregar una película
    
class ActualizarPelicula(UpdateView):
    model = Pelicula
    template_name = 'peliculas/update.html'
    fields = ['titulo', 'director', 'descripcion', 'poster', 'actores_principales', 'fecha_salida', 'genero', 'clasificacion', 'idiomas',
              'duracion', 'estrellas']
    success_url = reverse_lazy('listar-peliculas')
    
class EliminarPelicula(DeleteView):
    model = Pelicula
    template_name = 'peliculas/delete.html'
    success_url = reverse_lazy('listar-peliculas')