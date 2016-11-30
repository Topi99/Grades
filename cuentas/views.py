from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import UserRegistroForm

from .models import Profesor, Alumno, Padre

class Registro(View):
	def get(self, request):
		template_name = 'registro.html'
		form = UserRegistroForm()

		context = {
			'form':form
		}

		return render(request, template_name, context)

	def post(self, request):
		template_name = 'registro.html'
		q = request.POST['tipo']

		new_user_form = UserRegistroForm(request.POST)

		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()

			if q == 'prof':
				print("como profesor")
				perfil = Profesor()

			elif q == 'alumno':
				print("como alumno")
				perfil = Alumno()

			elif q == 'padre':
				print("como padre")
				perfil = Padre()

			perfil.user = new_user
			perfil.save()

			return redirect('perfil')

		else:
			print("Error")
			return render(request, template_name)
