from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^padres/$', views.PadreListView.as_view(), name="padre_list"),
]