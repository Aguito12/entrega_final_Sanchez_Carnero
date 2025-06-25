from django import forms
from .models import Profesional, Cliente, Tratamiento, Reserva, Consulta

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'especialidad', 'experiencia']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre', 'descripcion', 'precio', 'profesional']

class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cliente")

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'tratamiento', 'fecha', 'hora']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre', 'email', 'mensaje']



