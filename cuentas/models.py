from django.db import models
from django.conf import settings

class Profesor(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth = models.DateField(blank=True, null=True)
	cover = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	bio = models.TextField(blank=True, null=True)
	tel = models.IntegerField(default=000, blank=True, null=True)
	tipo = models.CharField(default='Profesor', max_length=8)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)

class Padre(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth = models.DateField(blank=True, null=True)
	cover = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	bio = models.TextField(blank=True, null=True)
	tel = models.IntegerField(default=000, blank=True, null=True)
	tipo = models.CharField(default='Padre', max_length=8)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)

class Alumno(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth = models.DateField(blank=True, null=True)
	cover = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	bio = models.TextField(blank=True, null=True)
	tel = models.IntegerField(default=000, blank=True, null=True)
	profesor = models.ForeignKey(Profesor, related_name='alumnos')
	padre = models.ForeignKey(Padre, related_name='hijos')
	tipo = models.CharField(default='Alumno', max_length=8)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)


