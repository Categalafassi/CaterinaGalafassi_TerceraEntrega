from inicio.views import inicio, saludo, crear_libro, listado_de_libros
from django.urls import path

urlpatterns = [
    path('',inicio, name='inicio'),
    path('saludo/<str:nombre>/', saludo, name='saludo'),
    path('inicio/crear-libro', crear_libro, name='crear_libro'),
    path('inicio/listado-de-libros', listado_de_libros, name='listado_de_libros')
]