from django.db import models

# Create your models here.

class Libro:
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ISBN=models.IntegerField(max_length=13)
    fecha_publicacion=models.DateField()
    sinopsis=models.TextField(null=True, blank=True)
    