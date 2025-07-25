from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

