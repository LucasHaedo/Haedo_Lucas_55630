"""
URL configuration for Valoralo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from valoralo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cargar_pelicula/', views.cargar_pelicula, name='cargar_pelicula'),
    path('lista_peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('valorar_pelicula/<int:pelicula_id>/', views.valorar_pelicula, name='valorar_pelicula'),
    path('cargar_productos/', views.cargar_productos, name='cargar_productos'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('modificar_datos/', views.modificar_datos, name='modificar_datos'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('shop/', views.shop, name='shop'),
    path('perfil/', views.perfil, name='perfil'), 
    path('modificar_datos/', views.modificar_datos, name='modificar_datos'),
    path('shop/', views.shop, name='shop'),
    path('comprar_producto/<int:id>/', views.comprar_producto, name='comprar_producto'),
    path('valorar_pelicula/<int:pelicula_id>/', views.valorar_pelicula, name='valorar_pelicula'),
]
