from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Cliente, Profesional, Tratamiento, Reserva, Consulta

# ---------------------------
# CLIENTE
# ---------------------------
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'acciones')

    def acciones(self, obj):
        ver_url = reverse('admin:AppCoder_cliente_change', args=[obj.pk])
        editar_url = reverse('admin:AppCoder_cliente_change', args=[obj.pk])
        eliminar_url = reverse('admin:AppCoder_cliente_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" style="background-color:#198754; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Ver</a>'
            '<a href="{}" style="background-color:#0d6efd; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Editar</a>'
            '<a href="{}" style="background-color:#dc3545; color:white; padding:4px 8px; border-radius:4px; text-decoration:none;">Eliminar</a>',
            ver_url, editar_url, eliminar_url
        )
    acciones.short_description = 'Acciones'


# ---------------------------
# PROFESIONAL
# ---------------------------
@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'experiencia', 'acciones')

    def acciones(self, obj):
        ver_url = reverse('admin:AppCoder_profesional_change', args=[obj.pk])
        editar_url = reverse('admin:AppCoder_profesional_change', args=[obj.pk])
        eliminar_url = reverse('admin:AppCoder_profesional_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" style="background-color:#198754; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Ver</a>'
            '<a href="{}" style="background-color:#0d6efd; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Editar</a>'
            '<a href="{}" style="background-color:#dc3545; color:white; padding:4px 8px; border-radius:4px; text-decoration:none;">Eliminar</a>',
            ver_url, editar_url, eliminar_url
        )
    acciones.short_description = 'Acciones'


# ---------------------------
# TRATAMIENTO
# ---------------------------
@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'profesional', 'acciones')

    def acciones(self, obj):
        ver_url = reverse('admin:AppCoder_tratamiento_change', args=[obj.pk])
        editar_url = reverse('admin:AppCoder_tratamiento_change', args=[obj.pk])
        eliminar_url = reverse('admin:AppCoder_tratamiento_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" style="background-color:#198754; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Ver</a>'
            '<a href="{}" style="background-color:#0d6efd; color:white; padding:4px 8px; border-radius:4px; text-decoration:none; margin-right:5px;">Editar</a>'
            '<a href="{}" style="background-color:#dc3545; color:white; padding:4px 8px; border-radius:4px; text-decoration:none;">Eliminar</a>',
            ver_url, editar_url, eliminar_url
        )
    acciones.short_description = 'Acciones'


# ---------------------------
# RESERVA
# ---------------------------
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tratamiento', 'fecha', 'hora')
    list_filter = ('fecha', 'tratamiento')
    search_fields = ('cliente__nombre', 'tratamiento__nombre')


# ---------------------------
# CONSULTA
# ---------------------------
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje')
    search_fields = ('nombre', 'email')



