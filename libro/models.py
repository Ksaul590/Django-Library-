from django.db import models
from autor.models import Autor
from categoria.models import Categoria

class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    anio_publicacion = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo