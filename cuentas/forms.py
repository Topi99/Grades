from django import forms
from django.contrib.auth.models import User
from .models import Profesor, Alumno, Padre 

class UserRegistroForm(forms.ModelForm):
	password = forms.CharField(label="Contrasena", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirma tu contrasena", widget=forms.PasswordInput)

	class Meta():
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email' )

class PadreForm(forms.ModelForm):
	class Meta():
		model = Padre
		fields = ('birth', 'cover', 'avatar', 'bio', 'tel')

class ProfesorForm(forms.ModelForm):
	class Meta():
		model = Profesor
		fields = ('birth', 'cover', 'avatar', 'bio', 'tel')

class AlumnoForm(forms.ModelForm):
	class Meta():
		model = Alumno
		fields = ('birth', 'cover', 'avatar', 'bio', 'tel')