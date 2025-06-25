from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),  # Asegurate que coincida el nombre de la app
]