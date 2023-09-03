from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pelicula, Producto, Imagen, Valoracion

admin.site.register(Pelicula)
admin.site.register(Producto)
admin.site.register(Imagen)
admin.site.register(Valoracion)