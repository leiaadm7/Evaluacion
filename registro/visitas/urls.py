from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_visita, name='registrar_visita'),
    path('listar/', views.listar_visitas, name='listar_visitas'),
]
