from django import forms
from .models import *


class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aeropuerto  # Asociamos el formulario con el modelo Aeropuerto
        fields = ['nombre', 'ciudad', 'codigo', 'capacidad']  # Campos del modelo que queremos incluir en el formulario

