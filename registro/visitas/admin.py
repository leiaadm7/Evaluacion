from django.contrib import admin
from .models import Visita
from django.utils import timezone

# Configura cómo se verá el modelo Visita en el panel de administración
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','rut', 'motivo', 'hora_entrada', 'hora_salida','estado')# columnas visibles
    search_fields = ('rut', 'nombre', 'apellido') #permite buscar
    list_filter = ('fecha', 'estado') # filtros en el panel
    actions = ['marcar_salida'] #acciones masivas

#Acción personalizada: marcar salida
@admin.action(description='Marcar visitas seleccionadas como finalizadas')
def marcar_salida(self, request, queryset):
    for visita in queryset.filter(estado='EN_CURSO'):
        visita.estado = 'FINALIZADA'
        visita.hora_salida = timezone.now()
        visita.save()
