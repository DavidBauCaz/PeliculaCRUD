from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pelicula
from django.urls import reverse_lazy

#vista para mostrar las películas
class ListarPeliculas(ListView):
    model = Pelicula
    template_name = "peliculas/read.html"
    context_object_name = "peliculas"
    
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
    success_url = reverse_lazy('listar-peliculas')
    
class ActualizarPelicula(UpdateView):
    model = Pelicula
    template_name = 'templates/update.html'
    fields = ['titulo', 'director', 'descripcion', 'poster', 'actores_principales', 'fecha_salida', 'genero', 'clasificacion', 'idiomas',
              'duracion', 'estrellas']
    success_url = reverse_lazy('listarPeliculas')
    
class EliminarPelicula(DeleteView):
    model = Pelicula
    template_name = 'templates/delete.html'