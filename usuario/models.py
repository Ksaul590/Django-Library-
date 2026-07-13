from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField( max_length=10, unique=True)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"