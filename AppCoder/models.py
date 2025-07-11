from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone   # ✅ IMPORT para default de fecha

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    experiencia = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)  # ✅ 2° CharField adicional
    descripcion = RichTextField()  # ✅ texto enriquecido
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tratamientos/', blank=True, null=True)  # ✅ campo imagen
    fecha = models.DateField(default=timezone.now)   # ✅ default agregado

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.cliente} - {self.tratamiento} ({self.fecha} {self.hora})"

class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f"Consulta de {self.nombre}"


