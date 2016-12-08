from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, TemplateView, View
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Grupo, Materia, Parcial, Calificacion

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import GruposForm

'''
@method_decorator(login_required, name='dispatch')
class GruposList(ListView):

	context_object_name = 'grupos'	
	template_name = 'grupos/grupos_list.html'

	def get_queryset(self):
		try:
			if self.request.user.profesor:
				queryset = Grupo.objects.filter(profesor=self.request.user.profesor)
			elif self.request.user.alumno:
				queryset = Grupo.objects.filter(profesor=self.request.user.alumno)
			elif self.request.user.padre:
				queryset = Grupo.objects.filter(profesor=self.request.user.padre)
		except:
			print('Error')
'''

@method_decorator(login_required, name='get')
class GruposList(View):
	def get(self, request):
		template_name = 'grupos/grupos_list.html'
		try:
			if request.user.profesor:
				grupos=request.user.profesor.grupos.all()
		except:
			print('No eres profesor')
		try:
			if request.user.alumno:
				grupos=request.user.alumno.grupos.all()
		except:
			print('No eres alumno')
		context = {
			'grupos':grupos
		}

		return render(request, template_name, context)

# @method_decorator(login_required, name='get')
class GruposCreate(View):
	def get(self, request):
		template_name = 'grupos/grupos_form.html'
		form = GruposForm()
		context = {
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = 'grupos/grupos_form.html'
		new_group_form = GruposForm(request.POST)

		if new_group_form.is_valid():
			new_group = new_group_form.save(commit=False)
			new_group.save()
			new_group.profesores.add(request.user.profesor)
			new_group_form.save_m2m()

			return redirect('boletas:grupos')	
		else:
			form = GruposForm()
			context = {
				'form':form
			}
			return render(request, template_name, context)	