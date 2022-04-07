from django.db import models


# Create your models here.
class Cat_Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    num_parte = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    disco = models.CharField(max_length=100)
    comentario = models.CharField(max_length=255)

    def __str__(self):
        return f'Equipo {self.id}: {self.marca} {self.modelo}'
