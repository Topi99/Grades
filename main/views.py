from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
	template_name = 'main/index.html'
