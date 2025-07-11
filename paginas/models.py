from django.db import models
from ckeditor.fields import RichTextField

class Promocion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='promociones/', blank=True, null=True)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo


