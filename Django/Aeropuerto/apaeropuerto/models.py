from django.db import models
from django.utils  import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, RegexValidator



# Modelo Aeropuerto
class Aeropuerto(models.Model):
    PAISES = [
    ("ES", "España"),
    ("FR", "Francia"),
    ("IT", "Italia"),
    ("DE", "Alemania"),
    ("PT", "Portugal"),
    ("NL", "Países Bajos"),
    ("BE", "Bélgica"),
    ("SE", "Suecia"),
    ("AT", "Austria"),
    ("CH", "Suiza"),
    ]
    CIUDADES = [
    ("ES", "Madrid"),
    ("FR", "París"),
    ("IT", "Roma"),
    ("DE", "Berlín"),
    ("PT", "Lisboa"),
    ("NL", "Ámsterdam"),
    ("BE", "Bruselas"),
    ("SE", "Estocolmo"),
    ("AT", "Viena"),
    ("CH", "Ginebra"),
    ]


    nombre = models.CharField(
        max_length=100,
        verbose_name="Aeropuerto"
    )
    ciudades = models.CharField(
        max_length=2,
        choices=CIUDADES,default='ES'
    ) 
    pais = models.CharField(
        max_length=2,
        choices=PAISES, default='ES'
    ) 
    capacidad_maxima = models.IntegerField(default=150) # Campo por defecto

    def __str__(self):
        return self.nombre
    
#Modelo ContactoAeropuerto
class ContactoAeropuerto(models.Model):
    aeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15, blank=True)
    email_contacto = models.EmailField(blank=True)

    def __str__(self):
        return f"Contacto de {self.aeropuerto.nombre}"


# Modelo Aerolínea
class Aerolinea(models.Model):

    paises = [
        ("ES", "España"),
        ("EN", "Inglaterra"),
        ("FR", "Francia"),
        ("IT", "Italia"),
    ]

    nombre = models.CharField(max_length=100,verbose_name="Aerolínea operadora")
    codigo = models.CharField(max_length=10)
    fecha_fundacion = models.DateField(auto_now_add=True)
    pais = models.CharField(
        max_length=2,
        choices=paises,default='ES'
    )
    aeropuerto =   models.ManyToManyField(Aeropuerto) # Relación ManytoMany

    def __str__(self):
        return self.nombre    


# Modelo Vuelo
class Vuelo(models.Model):
    hora_salida = models.DateTimeField(blank=False,error_messages={'blank': 'Este campo no puede estar vacío.',})
    hora_llegada = models.DateTimeField(blank=False,error_messages={'blank': 'Este campo no puede estar vacío.',})
    estado  = models.BooleanField(db_column='Volando') #boolean
    duracion = models.DurationField(editable=False)  # Duración del vuelo

    origen = models.ManyToManyField(Aeropuerto , related_name='vuelos_de_origen') # ManyToMany
    destino = models.ManyToManyField(Aeropuerto ,related_name='vuelos_de_destino') #ManyToMany
    aerolinea = models.ManyToManyField(Aerolinea , through='VueloAerolinea') # tabla intermedia

    

    def save(self, *args, **kwargs):
        # Calcular la duración como la diferencia entre hora_llegada y hora_salida
        if self.hora_llegada and self.hora_salida:
            self.duracion = self.hora_llegada - self.hora_salida
        super().save(*args, **kwargs)

# Modelo EstadisticasVuelo
class EstadisticasVuelo(models.Model):
    vuelo = models.OneToOneField(Vuelo, on_delete=models.CASCADE)
    numero_asientos_vendidos = models.IntegerField(default=0)
    numero_cancelaciones = models.IntegerField(default=0)
    feedback_pasajeros = models.TextField(blank=True)

    def __str__(self):
        return f"Estadísticas de Vuelo {self.vuelo.id}"


# Modelo Pasajero
def validar_dominio_email(email):
    # Lista de dominios permitidos
        dominios_permitidos = ['@gmail.com', '@hotmail.com', '@polignosur.org']
    
    # Comprobar si el correo electrónico termina con alguno de los dominios permitidos
        if not any(email.endswith(dominio) for dominio in dominios_permitidos):
            raise ValidationError(
                _('El correo electrónico debe tener uno de los siguientes dominios: @gmail.com, @hotmail.com, @polignosur.org.'),
                code='invalid_domain',
            )
        
class Pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, blank=True)  # Permitir valores vacíos
    email = models.EmailField(validators=[validar_dominio_email])
    telefono = models.CharField(
        max_length=9,
        validators=[
            MaxLengthValidator(9),
            RegexValidator(regex=r'^\d{9}$', message='El número de teléfono debe tener exactamente 9 dígitos.')
        ],
        blank=True  # Permitir que este campo esté vacío si es necesario
    )
    fecha_nacimiento = models.DateField(null=True)  
    vuelo = models.ManyToManyField(Vuelo, related_name='vuelo_pasajero') # Relación Many To Many
    


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
#Modelo OnetoOne Pasajero       
class PerfilPasajero(models.Model):
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True)
    documento_identidad = models.CharField(max_length=20, unique=True)
    nacionalidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Perfil de {self.pasajero.nombre} {self.pasajero.apellido}"

    
# Modelo Equipaje
class Equipaje(models.Model):
    peso = models.FloatField()
    dimensiones = models.CharField(max_length=50)
    tipo_material = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)  # Relación OneToOne

    def __str__(self):
        return f"Equipaje de {self.pasajero.nombre} {self.pasajero.apellido}"



# Tabla intermedia Vuelo_Aerolinea
class VueloAerolinea(models.Model):
    tipos_clase_avion = [
    ("E", "Economy"),
    ("B", "Business"),
    ("F", "First Class"),
    ("P", "Premium Economy"),
    ("L", "Luxury"),
    ("S", "Standard"),
    ("H", "Hybrid"),
    ("X", "Extra Legroom"),
    ("R", "Regional"),
    ("C", "Charter")
    ]

    fecha_operacion = models.DateTimeField(null=True)
    estado = models.TextField()
    clase = models.CharField(max_length=1,choices=tipos_clase_avion, default='E')
    incidencias = models.CharField(max_length=100)

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación Many To One
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE) # Relación Many To One
  


# Modelo Reserva
class Reserva(models.Model):

    METODO_PAGO_CHOICES = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('efectivo', 'Efectivo'),
        ('paypal', 'PayPal'),
    ]
    fecha_reserva = models.DateTimeField(default=timezone.now)  # Valor por defecto: fecha y hora actuales
    estado = models.CharField(max_length=50,help_text="Introduce Como va el avion durante el vuelo")
    metodo_pago = models.CharField(max_length=10, 
                                   choices=METODO_PAGO_CHOICES,
                                   default= 'tarjeta')
    estado_de_pago = models.BooleanField(default=False)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)  # Relación ManyToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne

    def __str__(self):
        return f"Reserva de {self.pasajero.nombre} {self.pasajero.apellido}"


# Modelo Silla (para Vuelo)
class Silla(models.Model):
    tipos_clase_avion = [
    ("E", "Economy"),
    ("B", "Business"),
    ("F", "First Class"),
    ("P", "Premium Economy"),
    ("L", "Luxury"),
    ("S", "Standard"),
    ("H", "Hybrid"),
    ("X", "Extra Legroom"),
    ("R", "Regional"),
    ("C", "Charter")
    ]

    clase = models.CharField(max_length=1,choices=tipos_clase_avion,default='E')
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    posicion = models.CharField(max_length=100)
    estado = models.BooleanField()

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)  # Relación ManyToOne
    pasajero = models.ForeignKey(Pasajero,on_delete=models.CASCADE)  # Relación ManyToOne 

    def __str__(self):
        return f"Silla {self.numero} ({self.clase})"


# Modelo Servicio
class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    costo = models.FloatField()
    duracion_servicio = models.TimeField()
    añadido = models.CharField(max_length=100)

    aeropuerto = models.ManyToManyField(Aeropuerto)  # Relación Many To Many

    def __str__(self):
        return self.tipo_servicio
    

# Modelo Empleado
class Empleado(models.Model):
    CARGO = [
        ('JE', 'Jefe'),
        ('EM', 'Empleado'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=2,choices=CARGO,default='EM')
    fecha_contratacion = models.DateField()
    
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE , related_name = 'empleado_servicio') #Many To One


    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo}"