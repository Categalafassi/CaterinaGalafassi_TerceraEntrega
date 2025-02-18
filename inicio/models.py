from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ISBN=models.IntegerField()
    fecha_publicacion=models.DateField()
    sinopsis=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} {self.autor} {self.ISBN} {self.fecha_publicacion} {self.sinopsis}"