from django.db import models
from django.contrib.auth.models import User  
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.db.models import Avg


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='peliculas/')
    descripcion = models.TextField()
    valoraciones = models.ManyToManyField('Valoracion', related_name='peliculas_valoradas')
    promedio = models.FloatField(null=True, blank=True) # Agregar el campo promedio
    cantidad = models.IntegerField(default=0) # Agregar el campo cantidad

class Valoracion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagenes = models.ManyToManyField('Imagen')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ventas = models.IntegerField(default=0)

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='productos/') 

class Consulta(models.Model):
    consulta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.IntegerField(default=1)


@receiver(post_save, sender=Valoracion)
def actualizar_pelicula(sender, instance, **kwargs):
    # instance es la instancia de Valoracion que se ha guardado
    pelicula = instance.pelicula # La película a la que pertenece la valoración
    valoraciones = pelicula.valoraciones.all() # Todas las valoraciones de la película
    promedio = valoraciones.aggregate(Avg('valoracion'))['valoracion__avg'] # El promedio de las valoraciones
    cantidad = valoraciones.count() # La cantidad de valoraciones
    pelicula.promedio = promedio # Actualizar el atributo promedio del modelo Pelicula
    pelicula.cantidad = cantidad # Actualizar el atributo cantidad del modelo Pelicula
    pelicula.save() # Guardar los cambios en el modelo Pelicula