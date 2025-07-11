from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Promocion

class PromocionListView(ListView):
    model = Promocion
    template_name = 'promociones/listado_promociones.html'
    context_object_name = 'promociones'

class PromocionDetailView(DetailView):
    model = Promocion
    template_name = 'promociones/detalle_promocion.html'
    context_object_name = 'promocion'

class PromocionCreateView(LoginRequiredMixin, CreateView):
    model = Promocion
    template_name = 'promociones/promocion_form.html'
    fields = ['titulo', 'subtitulo', 'descripcion', 'imagen', 'fecha']
    success_url = reverse_lazy('promociones-list')

class PromocionUpdateView(LoginRequiredMixin, UpdateView):
    model = Promocion
    template_name = 'promociones/promocion_form.html'
    fields = ['titulo', 'subtitulo', 'descripcion', 'imagen', 'fecha']
    success_url = reverse_lazy('promociones-list')

class PromocionDeleteView(LoginRequiredMixin, DeleteView):
    model = Promocion
    template_name = 'promociones/promocion_confirm_delete.html'
    success_url = reverse_lazy('promociones-list')



