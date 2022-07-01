from operator import mod
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+" "+str(self.camada)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+str(self.apellido)

class Entregable(models.Model):
    fechaDeEntregable = models.DateField()
    entregado = models.BooleanField

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    materia = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.apellido)+" "+str(self.materia)

