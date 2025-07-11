from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('buscar-cliente/', views.buscar_cliente, name="BuscarCliente"),
    path('tratamientos-disponibles/', views.ver_tratamientos, name="VerTratamientos"),
    path('profesionales-disponibles/', views.ver_profesionales, name="VerProfesionales"),
    path('reservar-tratamiento/', views.hacer_reserva, name="ReservarTratamiento"),
    path('enviar-consulta/', views.enviar_consulta, name="EnviarConsulta"),
    path('gracias/', views.gracias, name="Gracias"),
    # Rutas protegidas (solo superusuario)
    path('profesional/', views.agregar_profesional, name="Profesional"),
    path('cliente/', views.agregar_cliente, name="Cliente"),
    path('tratamiento/', views.agregar_tratamiento, name="Tratamiento"),
    ] 