
# Create your views here.
from django.shortcuts import render, redirect
from .models import Pelicula
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Imagen 
from django.shortcuts import render, get_object_or_404
from .models import Pelicula
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserCreationForm 
from .forms import UserForm,ValoracionForm
from .models import Consulta 
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto 
from django.db.models import Avg
from .models import Valoracion 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pelicula, Valoracion
from .forms import ValoracionForm
@login_required
def cargar_pelicula(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        imagen = request.FILES['imagen']
        descripcion = request.POST['descripcion']
        valoracion = request.POST['valoracion']
        pelicula = Pelicula(titulo=titulo, imagen=imagen, descripcion=descripcion, valoracion=valoracion)
        pelicula.save()
        return redirect('lista_peliculas')
    return render(request, 'cargar_pelicula.html')

@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    peliculas_valoradas = []
    for pelicula in peliculas:
        valoraciones = pelicula.valoraciones.all()
        if valoraciones:
            promedio = valoraciones.aggregate(Avg('valoracion'))['valoracion__avg']
            cantidad = valoraciones.count()
            form = ValoracionForm()
            estrellas = range(int(promedio))
            peliculas_valoradas.append((pelicula, promedio, cantidad, form, estrellas))
        else:
            form = ValoracionForm()
            peliculas_valoradas.append((pelicula, None, 0, form, []))
    return render(request, 'lista_peliculas.html', {'peliculas': peliculas_valoradas})


@login_required
def cargar_productos(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        imagenes = request.FILES.getlist('imagenes')
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        producto = Producto(titulo=titulo, descripcion=descripcion, precio=precio)
        producto.save()
        for imagen in imagenes:
            imagen_obj = Imagen(imagen=imagen)
            imagen_obj.save()
            producto.imagenes.add(imagen_obj)
        return redirect('lista_productos')
    return render(request, 'cargar_productos.html')

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

from django.shortcuts import redirect

@login_required
def valorar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    if request.method == 'POST':
        form = ValoracionForm(request.POST)
        if form.is_valid():
            valoracion = Valoracion.objects.create(
                pelicula=pelicula,
                usuario=request.user,
                valoracion=form.cleaned_data['valoracion'],
                comentario=form.cleaned_data.get('comentario', '')
            )
            print(f'Se guardó la valoración: {valoracion}')
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                promedio = round(pelicula.valoraciones.aggregate(Avg('valoracion'))['valoracion__avg'], 1)
                cantidad = pelicula.valoraciones.count()
                return JsonResponse({
                    'message': 'Gracias por valorar esta película',
                    'promedio': promedio,
                    'cantidad': cantidad
                })
    else:
        form = ValoracionForm()
    return render(request, 'valorar_pelicula.html', {'pelicula': pelicula, 'form': form})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('menu'))
        else:
            messages.error(request, 'El usuario y/o contraseña no son válidos')
    return render(request, 'login.html')



@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def shop(request):
    productos = Producto.objects.all()
    consultas = Consulta.objects.all() # Aquí puedes obtener la lista de consultas
    context = {'productos': productos, 'consultas': consultas}
    return render(request, 'shop.html', context)


@login_required
def detalle_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        # Aquí puedes procesar la compra del producto por parte del usuario
        # Por ejemplo, puedes actualizar el inventario o crear un registro de la compra
     return render(request, 'detalle_producto.html', {'producto': producto})
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def modificar_datos(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada con éxito')
            return redirect('home')
        else:
            messages.error(request, 'Ha ocurrido un error al cambiar tu contraseña')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'modificar_datos.html', {'form': form})
def home(request):
    return render(request, 'home.html')

@login_required
def menu(request):
    peliculas = Pelicula.objects.all().order_by('-id')[:4] # Obtener las últimas 4 películas
    for pelicula in peliculas:
        valoracion_promedio = pelicula.valoraciones.aggregate(Avg('valoracion'))['valoracion__avg']
        pelicula.valoracion = round(valoracion_promedio, 1) if valoracion_promedio else None # Calcular el promedio de valoración y redondearlo a 1 decimal
        pelicula.cantidad = pelicula.valoraciones.count() # Contar las valoraciones
    productos = Producto.objects.all().order_by('?')[:4] # Obtener 4 productos aleatorios
    return render(request, 'menu.html', {'peliculas': peliculas, 'productos': productos})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos han sido modificados con éxito')
            # Redirige al usuario a la misma página para mostrar los cambios
            return redirect('perfil')
        else:
            messages.error(request, 'Ha ocurrido un error al modificar tus datos')
    else:
        form = UserForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'perfil.html', context) 

@csrf_exempt
@login_required
def enviar_consulta(request):
    if request.method == 'POST':
        consulta = request.POST.get('consulta')
        print("Consulta recibida:", consulta)
        nueva_consulta = Consulta(consulta=consulta, usuario=request.user) 
        nueva_consulta.save()
        return JsonResponse({'mensaje': 'Consulta enviada'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'})
    

def comprar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'comprar_producto.html', {'producto': producto})