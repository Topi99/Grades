from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.GruposList.as_view(), name="grupos"),
	url(r'^grupo/crear$', views.GruposCreate.as_view(), name="crear_grupo")
]