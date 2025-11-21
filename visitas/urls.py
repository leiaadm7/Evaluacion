from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"visita", views.VisitaViewSet)

app_name = 'visitas'
urlpatterns = [
    path("api/", include(router.urls)),
    path('', views.inicio, name='inicio'), # Página de inicio
    path('registrar/', views.registrar_visita, name='registrar_visita'), # Página para registrar una nueva visita
    path('listar/', views.listar_visitas, name='listar_visitas'), # Página para listar visitas
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'), # Marcar salida
    path('eliminar/<int:pk>/', views.eliminar_visita, name='eliminar_visita'), # Eliminar visita
    path('editar/<int:pk>/', views.editar_visita, name='editar_visita'), # Para editar
]
