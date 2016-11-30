from django import forms
from django.contrib.auth.models import User 

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