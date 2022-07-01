from cmath import inf
import email
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor
from django.template import loader
from AppCoder.forms import CursoFormulario, EstudianteFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def curso(self):
    curso = Curso(nombre="Lengua", camada=22)
    curso.save()
    documento = f"Curso: {curso.nombre} -- Camada: {curso.camada}"
    return HttpResponse(documento)

def cursos(request):
    return render (request, 'appCoder/cursos.html')

def estudiante(request):
    return render (request, 'appCoder/estudiante.html')

def entregable(request):
    return render (request, 'appCoder/entregable.html')

def profesor(request):
    return render (request, 'appCoder/profesor.html')


def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['curso']
        camada = informacion['camada']
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()    
    return render(request, 'appCoder/cursoFormulario.html', {'miFormulario': miFormulario})

def busquedaCamada(request):
    return render(request, 'appCoder/busquedaCamada.html') 

def buscar(request):
    #respuesta = f"Buscó la comisión {request.GET['camada']}"
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'appCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = "No ha ingresado una comisión existente"
    return HttpResponse(respuesta)

def leerEstudiantes (request):
    estudiante = Estudiante.objects.all()
    contexto = {'estudiante': estudiante}
    return render(request, 'AppCoder/estudiante.html', contexto) 

def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
        estudiante.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = EstudianteFormulario()    
    return render(request, 'appCoder/estudianteFormulario.html', {'miFormulario': miFormulario})

def eliminarEstudiante(request, nombre):
    estudiante = Estudiante.objects.get(nombre=nombre)
    estudiante.delete()
    estudiante = Estudiante.objects.all()
    contexto = {'estudiante': estudiante}
    return render(request, 'appCoder/estudiante.html', contexto)

def editarEstudiante(request, nombre):
    estudiante = Estudiante.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        estudiante.nombre = informacion['nombre']
        estudiante.apellido = informacion['apellido']
        estudiante.email = informacion['email']
        estudiante.save()

        estudiante = Estudiante.objects.all()
        contexto = {'estudiante': estudiante}
        return render(request, 'appCoder/estudiante.html', contexto)
    else:
        miFormulario = EstudianteFormulario(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
        contexto= {'miFormulario': miFormulario, 'nombre': nombre}
        return render(request, 'appCoder/editarEstudiante.html', contexto)


class ProfesoresList(ListView):
    model = Profesor
    template_name = 'AppCoder/profesor_list.html'

class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = 'AppCoder/profesor_detalle.html'

class ProfesorCreacion(CreateView):
    model = Profesor
    success_url = reverse_lazy('profesor_listar')
    fields = ['nombre', 'apellido', 'materia']

class ProfesorEdicion(UpdateView):
    model = Profesor
    success_url = reverse_lazy('profesor_listar')
    fields = ['nombre', 'apellido', 'materia']

class ProfesorEliminacion(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesor_listar')

