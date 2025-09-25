from django.db import models
from django.utils import timezone

#Modelo que guarda los datos de cada visita
class Visita(models.Model):
    nombre = models.CharField(max_length=20)#Nombre del visitante
    apellido = models.CharField(max_length=35)#Apellido del visitante
    rut = models.CharField(max_length=12)#RUT del visitante (identificacion chilena)
    motivo = models.TextField()#Motivo de la visita
    hora_entrada = models.DateTimeField(auto_now_add=True)#Hora de entrada que se guarda automáticamente al crear el registro
    hora_salida = models.DateTimeField(null=True, blank=True)#Hora de salida
    fecha = models.DateField(default=timezone.now)#Fecha de la visita automaticamente al crear el registro

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"
    
