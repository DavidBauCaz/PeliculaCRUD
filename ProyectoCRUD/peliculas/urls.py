from django.urls import path
from .views import ListarPeliculas, DetallesPelicula, CrearPelicula, ActualizarPelicula, EliminarPelicula

urlpatterns = [
    path('', ListarPeliculas.as_view(), name='listar-peliculas'), #mostramos la lista de peliculas
    path('<int:pk>/', DetallesPelicula.as_view(), name='read-pelicula'), #vemos todos los detalles de la pelicula
    path('crear/', CrearPelicula.as_view(), name='create-pelicula'), # añadimos una nueva pelicula a a base de datos
    path('<int:pk>/update/', ActualizarPelicula.as_view(), name='update-pelicula'), # actualizamos la información de una pelicula
    path('<int:pk>/delete',EliminarPelicula.as_view(), name='delete-pelicula' ), # eliminamos una pelicula de la base de datos
]