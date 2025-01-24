from django.urls import path
from .views import ListarPeliculas, DetallesPelicula, CrearPelicula, ActualizarPelicula, EliminarPelicula

urlpatterns = [
    path('', ListarPeliculas.as_view(), name='listar-peliculas'), # Mostramos la lista de peliculas
    path('<int:pk>/', DetallesPelicula.as_view(), name='read-pelicula'), # Muestra los detalles de una pelicula
    path('crear/', CrearPelicula.as_view(), name='create-pelicula'), # Agregamos una pelicula la la base de datos
    path('<int:pk>/update/', ActualizarPelicula.as_view(), name='update-pelicula'), # actualizamos la información de una pelicula
    path('<int:pk>/delete',EliminarPelicula.as_view(), name='delete-pelicula' ), # eliminamos una pelicula de la base de datos
]