from django import forms
from .models import Grupo

class GruposForm(forms.ModelForm):
	class Meta():
		model = Grupo
		fields = ('nombre',)