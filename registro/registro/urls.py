from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta al panel de administración de Django
    path('', include('visitas.urls')), # Incluye las rutas de la app "visitas"
]
