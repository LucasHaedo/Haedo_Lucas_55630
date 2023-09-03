from django.urls import path
from valoralo_app import views

urlpatterns = [
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
    path('perfil/', views.perfil, name='perfil'),
    path('shop/', views.shop, name='shop'),
    path('comprar_producto/<int:id>/', views.comprar_producto, name='comprar_producto'),
    path('valorar_pelicula/<int:pelicula_id>/', views.valorar_pelicula, name='valorar_pelicula'),
]
