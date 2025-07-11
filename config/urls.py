from django.contrib import admin
from django.urls import path, include
from core.views import about_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),
    path('Cuentas/', include('Cuentas.urls')),
    path('promociones/', include('paginas.urls')),
    path('about/', about_view, name='about'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
