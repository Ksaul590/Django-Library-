from django.db import models
from libro.models import Libro
from usuario.models import Usuario

class Prestamo(models.Model):

    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    libro = models.ForeignKey(Libro,on_delete=models.PROTECT)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"Prestamo #{self.codigo}"