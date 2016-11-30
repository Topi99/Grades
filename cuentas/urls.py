from django.conf.urls import url, include
from . import views

from .api import urls as UrlsAPICuentas

urlpatterns = [
	url(r'^registro/$', views.Registro.as_view(), name="registro"),
	url(r'^api/', include(UrlsAPICuentas, namespace="api")),
	url(r'^padres/$', views.PadresListView.as_view(), name="padres")
]