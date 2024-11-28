from django import forms
from .models import *


class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aeropuerto  # Asociamos el formulario con el modelo Aeropuerto
        fields = ['nombre', 'ciudades', 'pais', 'capacidad_maxima']  # Campos del modelo que queremos incluir en el formulario

        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Introduce el nombre del aeropuerto"
            }),
            "ciudades": forms.Select(attrs={"class": "form-control"}),
            "pais": forms.Select(attrs={"class": "form-control"}),
            "capacidad_maxima": forms.NumberInput(attrs={"class": "form-control"}),
            "fecha_inauguracion": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

        # Textos de ayuda
        help_texts = {
            "nombre": "Maximo 100 caracteres.",
            "capacidad_maxima": "Especifica la capacidad del aeropuerto.",
        }

    # Validación para el campo "nombre"
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) > 200:
            raise forms.ValidationError("El nombre del aeropuerto no puede exceder los 200 caracteres.")
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre del aeropuerto solo puede contener letras.")
        return nombre

    # Validación para el campo "capacidad_maxima"
    def clean_capacidad_maxima(self):
        capacidad = self.cleaned_data.get("capacidad_maxima")
        if capacidad <= 0:
            raise forms.ValidationError("La capacidad máxima debe ser un número positivo.")
        if capacidad > 100:
            raise forms.ValidationError("La capacidad máxima no puede exceder los 100 millones de pasajeros.")
        return capacidad