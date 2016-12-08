from django.conf.urls import url, include
from django.contrib import admin

from main import urls as UrlsMain
from cuentas import urls as UrlsCuentas
from boletas import urls as UrlsBoletas

from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(UrlsMain, namespace='main')),
    url(r'^accounts/', include(UrlsCuentas, namespace='cuentas')),
    url(r'^boletas/', include(UrlsBoletas, namespace='boletas')),
    url(
        regex=r'^media/(?P<path>.*)/$',
        view=serve,
        kwargs={"document_root":settings.MEDIA_ROOT}
        )
]
