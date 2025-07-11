from django.contrib import admin
from .models import Promocion

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')

