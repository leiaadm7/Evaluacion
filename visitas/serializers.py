from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Visita

class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = [
            "id",
            "url",
            "nombre",
            "apellido",
            "rut",
            "motivo",
            "hora_entrada",
            "hora_salida",
            "fecha",
            "estado",
            "registrado_por"
        ]

        # Se define 'view_name' con el prefijo 'visitas:' porque en urls.py usamos app_name. 
        # Así el serializer puede encontrar la ruta correcta.
        extra_kwargs = {
            'url': {'view_name': 'visitas:visita-detail'},
            'registrado_por': {'view_name': 'visitas:user-detail'}
        }
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

        extra_kwargs = {
            'url': {'view_name': 'visitas:user-detail'},
            'groups': {'view_name': 'visitas:group-detail'}
        }

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

        extra_kwargs = {
            'url': {'view_name': 'visitas:group-detail'}
        }