from django.db import models
from django.contrib.auth.models import User
from cuentas.models import Profesor, Alumno

class Grupo(models.Model):
	profesor = models.ManyToManyField(Profesor)
	alumno = models.ManyToManyField(Alumno, blank=True)
	nombre = models.CharField(max_length=30)

class Materia(models.Model):
	grupo = models.ForeignKey(Grupo, related_name='materias')
	nombre = models.CharField(max_length=30)

class Parcial(models.Model):
	materia = models.ForeignKey(Materia, related_name='parciales')
	numero = models.IntegerField(default=1)

class Calificacion(models.Model):
	parcial = models.ForeignKey(Parcial, related_name='calificaciones')
	alumno = models.ForeignKey(Alumno, related_name='calificaciones')
	valor = models.IntegerField(default=0)
