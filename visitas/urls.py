from django.urls import path
from . import views

app_name = 'visitas'

urlpatterns = [
    path('', views.inicio, name='inicio'), # Página de inicio
    path('registrar/', views.registrar_visita, name='registrar_visita'), # Página para registrar una nueva visita
    path('listar/', views.listar_visitas, name='listar_visitas'), # Página para listar visitas
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'), # Marcar salida
    path('eliminar/<int:pk>/', views.eliminar_visita, name='eliminar_visita'), # Eliminar visita
    path('editar/<int:pk>/', views.editar_visita, name='editar_visita'), # Para editar
]
