from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from .forms import UserRegistroForm, PadreForm, AlumnoForm, ProfesorForm, UserEditForm, AlumnoRegistroForm

from .models import Profesor, Alumno, Padre

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'cuentas/dashboard.html'
		
		try:
			if request.user.padre:
				form = PadreForm(instance=request.user.padre)
				print('Es padre')
		except:
			print('No es padre')

		try:
			if request.user.alumno:
				form = AlumnoForm(instance=request.user.alumno)
				print('Es alumno')
		except:
			print('No es alumno')

		try:
			if request.user.profesor:
				form = ProfesorForm(instance=request.user.profesor)
				print('Es profesor')
		except:
			print('No es profesor')

		context = {
			'form':form,
			'form_user':UserEditForm(instance=request.user),
		}

		return render(request, template_name, context)

	def post(self, request):
		template_name = 'cuentas/dashboard.html'

		user_form = UserEditForm(data=request.POST, instance=request.user) 
		try:
			if request.user.padre:
				profile_form = PadreForm(data=request.POST, files=request.FILES, instance=request.user.padre)
				cover = request.user.padre.cover
				print('Es padre')
		except:
			print('No es padre')

		try:
			if request.user.alumno:
				profile_form = AlumnoForm(data=request.POST, files=request.FILES, instance=request.user.alumno)
				cover = request.user.alumno.cover
				print('Es alumno')
		except:
			print('No es alumno')

		try:
			if request.user.profesor:
				profile_form = ProfesorForm(data=request.POST, files=request.FILES, instance=request.user.profesor)
				cover = request.user.profesor.cover
				print('Es profesor')
		except:
			print('No es profesor')

		if user_form.is_valid() and profile_form.is_valid():
			user_info = user_form.save(commit=False)
			profile_info = profile_form.save(commit=False)
			user_info.save()
			profile_info.save()
			context = {
				'form_user':user_form,
				'form':profile_form,
				'cover':cover
      }
			return render(request, template_name, context)
		else:
			context = {}
			return render(request, template_name, context)


class Registro(View):
	def get(self, request):
		template_name = 'registro.html'
		form = UserRegistroForm()

		context = {
			'form':form,
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

			elif q == 'padre':
				print("como padre")
				perfil = Padre()

			perfil.user = new_user
			perfil.save()

			return redirect('cuentas:perfil')

		else:
			print("Error")
			return render(request, template_name)

class RegistroAlumno(View):
	def get(self, request):
		template_name = 'registro_a.html'
		form = AlumnoRegistroForm()

		context = {
			'form':form,
		}

		return render(request, template_name, context)

	def post(self, request):
		template_name = 'registro.html'

		new_user_form = AlumnoRegistroForm(request.POST)

		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()

			perfil = Alumno()
			perfil.user = new_user
			perfil.padre = Padre.objects.get(id=int(new_user_form.cleaned_data['padre_id']))
			perfil.profesor = Profesor.objects.get(id=int(new_user_form.cleaned_data['profesor_id']))
			perfil.save()

			return redirect('cuentas:perfil')
		else:
			print("Error")
			return render(request, template_name)


class PadresListView(ListView):
	model = Padre

class ProfesListView(ListView):
	model = Profesor