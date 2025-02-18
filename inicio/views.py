from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Libro
from inicio.forms import CrearLibro, BuscarLibro


def inicio(request):
    
    # return HttpResponse("<h1>Hola soy la vista :)</h1>")
    return render(request, 'inicio/inicio.html')

def saludo(request, nombre):
    hora_actual=datetime.now()
    
    return render(request, 'inicio/saludo.html', {'hora':hora_actual, 'nombre': nombre})

def crear_libro(request):
    print(request.GET)
    print(request.POST)
    formulario=CrearLibro()
    if request.method == "POST":
        formulario=CrearLibro(request.POST)
        if formulario.is_valid():
            titulo=formulario.cleaned_data.get('titulo')
            autor=formulario.cleaned_data.get('autor')
            ISBN=formulario.cleaned_data.get('ISBN')
            fecha_publicacion=formulario.cleaned_data.get('fecha_publicacion')
            sinopsis=formulario.cleaned_data.get('sinopsis')
            nuevo_libro=Libro(titulo=titulo, autor=autor, ISBN=ISBN, fecha_publicacion=fecha_publicacion, sinopsis=sinopsis)
            nuevo_libro.save()
            return redirect("listado_de_libros")
    
    return render(request, 'inicio/crear_libro.html', {'formulario': formulario})

def listado_de_libros(request):
    libros = Libro.objects.all()
    formulario=BuscarLibro(request.GET)
    if formulario.is_valid():
        titulo_a_buscar=formulario.cleaned_data.get("titulo")
        libros=Libro.objects.filter(titulo__icontains=titulo_a_buscar)
    return render(request, 'inicio/listado_de_libros.html', {'libros': libros, 'formulario': formulario})