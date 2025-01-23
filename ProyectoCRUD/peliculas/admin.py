from django.contrib import admin
from .models import Pelicula
# Register your models here.

@admin.register(Pelicula)
class AdminPelicula(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'estrellas')
    search_fields = ('titulo', 'director')
    list_filter = ('genero', 'estrellas')