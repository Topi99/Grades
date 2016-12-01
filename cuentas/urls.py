from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import logout, logout_then_login, login


from .api import urls as UrlsAPICuentas

urlpatterns = [
	url(r'^registro/$', views.Registro.as_view(), name="registro"),
	url(r'^api/', include(UrlsAPICuentas, namespace="api")),
	url(r'^padres/$', views.PadresListView.as_view(), name="padres"),
	url(r'^profile/$', views.Dashboard.as_view(), name="perfil"),
	url(r'^login/$', login, name="login"),
  url(r'^logout/$', logout, name="logout"),
  url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),
]