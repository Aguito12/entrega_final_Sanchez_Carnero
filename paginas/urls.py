from django.urls import path
from .views import (
    PromocionListView,
    PromocionDetailView,
    PromocionCreateView,
    PromocionUpdateView,
    PromocionDeleteView,
)

urlpatterns = [
    path('', PromocionListView.as_view(), name='listado_promociones'),
    path('detalle/<int:pk>/', PromocionDetailView.as_view(), name='detalle_promocion'),
    path('crear/', PromocionCreateView.as_view(), name='crear_promocion'),
    path('editar/<int:pk>/', PromocionUpdateView.as_view(), name='editar_promocion'),
    path('eliminar/<int:pk>/', PromocionDeleteView.as_view(), name='eliminar_promocion'),
]

