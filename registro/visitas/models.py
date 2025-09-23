from django.db import models
from django.utils import timezone

class Visita(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=35, null=True, blank=True)
    rut = models.CharField(max_length=12)
    motivo = models.TextField()
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    fecha = models.DateField(default=timezone.now) 

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"