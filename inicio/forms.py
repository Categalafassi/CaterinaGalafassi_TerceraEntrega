from django import forms

class CrearLibro(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    ISBN=forms.IntegerField()
    fecha_publicacion=forms.DateField()
    sinopsis=forms.CharField(widget=forms.Textarea, required=False)
    
class BuscarLibro(forms.Form):
    titulo = forms.CharField(max_length=50,required=False)