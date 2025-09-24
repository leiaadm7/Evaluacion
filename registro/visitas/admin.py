from django.contrib import admin
from .models import Visita

# Configura cómo se verá el modelo Visita en el panel de administración
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'motivo', 'hora_entrada', 'hora_salida')# columnas visibles
    list_filter = ('hora_entrada',) # filtros en el panel
