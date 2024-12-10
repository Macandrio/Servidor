from django import forms
from .models import *

#----------------------------------------------------------------------------------------------------
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

        if Aeropuerto.objects.filter(nombre__iexact=nombre).exists():
            raise ValidationError("Ya existe un aeropuerto con este nombre.")
        if Aeropuerto.objects.filter(nombre__iexact=nombre).exists():
                    raise ValidationError("Ya existe un aeropuerto con este nombre.")

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
    

class AeropuertoBusqueda(forms.Form):
    nombre = forms.CharField(
        required=False,
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Introduce el nombre del aeropuerto"
        })
    )
    ciudades = forms.ChoiceField(
        required=False,
        label="Ciudad",
        choices=[("", "Seleccione una ciudad")] + Aeropuerto.CIUDADES,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    pais = forms.ChoiceField(
        required=False,
        label="País",
        choices=[("", "Seleccione un país")] + Aeropuerto.PAISES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    def clean(self):
        super().clean()

        nombre = self.cleaned_data.get('nombre')
        ciudades = self.cleaned_data.get('ciudades')
        pais = self.cleaned_data.get('pais')

        # Si todos los campos están vacíos, mostrar un error
        if nombre == '' and ciudades == '' and pais == '':
            self.add_error('nombre','El campo no puede estar vacio')
        if nombre.islower():
            self.add_error('nombre','El nombre no puede empezar por minuscula')

        return self.cleaned_data
    

#----------------------------------------------------------------------------------------------------

class estadisticasvuelo(ModelForm):
    class Meta:
        model=EstadisticasVuelo
        fields='__all__'
        labels= {
            "fecha_estadisticas" : ("Fecha de la estadistica"),
            "numero_asientos_vendidos" : ("Resultado de la los asientos vendidos"),
            "numero_cancelaciones" : ("Resultado de la los asientos cancelados"),
            "feedback_pasajeros" : ("Comentario del cliente"),
        }
        widgets = {
            "fecha_estadisticas" : forms.SelectDateWidget(),
            "numero_asientos_vendidos" : forms.TextInput(),
            "numero_cancelaciones" : forms.TextInput(),
            "feedback_pasajeros":forms.SelectDateWidget(),
        }
    
    def clean(self):
        
        super().clean()
        
        numero_asientos_vendidos =self.cleaned_data.get('numero_asientos_vendidos') 
        numero_cancelaciones = self.cleaned_data.get('numero_cancelaciones') 
        feedback_pasajeros = self.cleaned_data.get('feedback_pasajeros') 
        
        
        if(numero_cancelaciones > numero_asientos_vendidos):
            self.add_error("numero_cancelaciones","No puede ver mas asientos cancelados que vendidos")
            
        if(feedback_pasajeros < 200):
            self.add_error("feedback_pasajeros","Tiene que ser menor a 200 caracteres")
            
        return self.cleaned_data
