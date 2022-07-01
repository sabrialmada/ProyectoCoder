import email
from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=50)
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField() 
    