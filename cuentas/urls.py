from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^registro/$', views.Registro.as_view(), name="registro")
]