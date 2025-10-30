import re
from django import forms
from .models import Visita
from django.core.exceptions import ValidationError

#Formulario basado en el modelo visita
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'apellido', 'rut', 'motivo']
        
    # Validación personalizada para el RUT
    def clean_rut(self):
        rut = self.cleaned_data['rut'].strip()
        # Formato exacto: 8 números + guion + dígito verificador (0-9 o K)
        patron = r'^\d{7,8}-[\dkK]$'
        if not re.match(patron, rut):
            raise forms.ValidationError("El RUT debe tener el formato 12345678-9")
        return rut.upper()