from django.urls import path
from . import views

app_name = 'visitas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar/', views.registrar_visita, name='registrar_visita'),
    path('listar/', views.listar_visitas, name='listar_visitas'),
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'),
]
