from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo']

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if not rut.replace(".", "").replace("-", "").isdigit():
            raise forms.ValidationError("El RUT debe contener solo números, puntos o guion.")
        return rut
