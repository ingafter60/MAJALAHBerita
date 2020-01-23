from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	 url(r'', include('appmain.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:

	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)