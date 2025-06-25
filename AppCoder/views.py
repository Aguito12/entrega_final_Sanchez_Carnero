from django.shortcuts import render, redirect
from .models import Profesional, Cliente, Tratamiento
from .forms import ProfesionalForm, ClienteForm, TratamientoForm, BusquedaClienteForm, ReservaForm, ConsultaForm

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def agregar_profesional(request):
    form = ProfesionalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Inicio")
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Agregar Profesional"})

def agregar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Inicio")
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Agregar Cliente"})

def agregar_tratamiento(request):
    form = TratamientoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Inicio")
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Agregar Tratamiento"})

def buscar_cliente(request):
    form = BusquedaClienteForm(request.GET)
    resultados = []
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Cliente.objects.filter(nombre__icontains=nombre)
    return render(request, "AppCoder/busqueda.html", {"form": form, "resultados": resultados})

def ver_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, "AppCoder/ver_tratamientos.html", {"tratamientos": tratamientos})

def ver_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, "AppCoder/ver_profesionales.html", {"profesionales": profesionales})

def hacer_reserva(request):
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Gracias")
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Reservar Tratamiento"})

def enviar_consulta(request):
    form = ConsultaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Gracias")
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Enviar Consulta"})

def gracias(request):
    return render(request, "AppCoder/gracias.html")
