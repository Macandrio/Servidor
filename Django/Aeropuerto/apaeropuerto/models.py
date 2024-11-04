from django.db import models
from django.utils  import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator




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
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15, blank=True)
    email_contacto = models.EmailField(blank=True)
    años_trabajados = models.IntegerField(verbose_name="Años Trabajado", default=0)

    aeropuerto = models.OneToOneField(Aeropuerto, on_delete=models.CASCADE) #OneToOne

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
    aeropuerto =   models.ManyToManyField(Aeropuerto, related_name='aerolinea_de_aeropuerto') # Relación ManytoMany

    def __str__(self):
        return self.nombre    


# Modelo Vuelo
class Vuelo(models.Model):
    hora_salida = models.DateTimeField(blank=False,error_messages={'blank': 'Este campo no puede estar vacío.',})
    hora_llegada = models.DateTimeField(blank=False,error_messages={'blank': 'Este campo no puede estar vacío.',})
    estado  = models.BooleanField(db_column='Volando') #boolean
    duracion = models.DurationField(editable=False)  # Duración del vuelo

    origen = models.ForeignKey(Aeropuerto , on_delete=models.CASCADE ,related_name='vuelos_de_origen') # ManyToOne
    destino = models.ForeignKey(Aeropuerto , on_delete=models.CASCADE ,related_name='vuelos_de_destino') #ManyToOne
    aerolinea = models.ManyToManyField(Aerolinea , through='VueloAerolinea' , related_name='vuelo_aerolinea') # tabla ManyToMany intermedia

    def clean(self):
        # Verificar que el aeropuerto de origen y destino no sean el mismo
        if self.origen == self.destino:
            raise ValidationError("El aeropuerto de origen y destino no pueden ser el mismo.")

    def save(self, *args, **kwargs):
        # Calcular la duración como la diferencia entre hora_llegada y hora_salida
        if self.hora_llegada and self.hora_salida:
            self.duracion = self.hora_llegada - self.hora_salida
        super().save(*args, **kwargs)

# Modelo EstadisticasVuelo
class EstadisticasVuelo(models.Model):
    fecha_estadisticas = models.DateField(auto_now_add=True)  # Fecha en que se registraron las estadísticas
    numero_asientos_vendidos = models.IntegerField(default=0)
    numero_cancelaciones = models.IntegerField(default=0)

    feedback_pasajeros = models.TextField(blank=True)


    vuelo = models.OneToOneField(Vuelo, on_delete=models.CASCADE, related_name='vuelo_datos') #OneToOne


# Modelo Pasajero
def validar_dominio_email(email):
    # Lista de dominios permitidos
        dominios_permitidos = ['@gmail.com', '@hotmail.com', '@polignosur.org']
    
    # Comprobar si el correo electrónico termina con alguno de los dominios permitidos
        if not any(email.endswith(dominio) for dominio in dominios_permitidos):
            raise ValidationError(('El correo electrónico debe tener uno de los siguientes dominios: @gmail.com, @hotmail.com, @polignosur.org.'),
                code='invalid_domain',)
        
class Pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, blank=True)  # Permitir valores vacíos
    email = models.EmailField(validators=[validar_dominio_email])
    telefono = models.IntegerField(validators=[ MaxValueValidator(999999999)],blank=True )
    fecha_nacimiento = models.DateField(null=True)  
    vuelo = models.ManyToManyField(Vuelo, related_name='vuelo_pasajero') # Relación Many To Many
    


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
#Modelo PerfilPasajero       
class PerfilPasajero(models.Model):
    direccion = models.CharField(max_length=255, blank=True)
    documento_identidad = models.CharField(max_length=9, unique=True)
    nacionalidad = models.CharField(max_length=50, blank=True)
    vivienda = models.CharField(max_length=50, blank=True)

    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE, related_name='pasajero_datos')# Relación OneToOne

    def __str__(self):
        return "DNI" + self.documento_identidad

    
# Modelo Equipaje
class Equipaje(models.Model):
    peso = models.FloatField()
    dimensiones = models.CharField(max_length=50)
    tipo_material = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE , related_name='equipaje_pasajero')  # Relación ManyToOne

    def __str__(self):
        return "Es del pasajero" + self.pasajero.nombre

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

    fecha_operacion = models.DateTimeField(null=True , blank=True)
    estado = models.TextField()
    clase = models.CharField(max_length=1,choices=tipos_clase_avion, default='E')
    incidencias = models.CharField(max_length=100)

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='vuelo_media_aerolinea')  # Relación Many To One
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE, related_name='aerolinea_media_aerolinea') # Relación Many To One
  


# Modelo Reserva
class Reserva(models.Model):

    METODO_PAGO_CHOICES = [
        ('tarjeta', 'Tarjeta de crédito'),
        ('efectivo', 'Efectivo'),
        ('paypal', 'PayPal'),
    ]
    fecha_reserva = models.DateTimeField(default=timezone.now)  # Valor por defecto: fecha y hora actuales
    codigo_descueto = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=10, 
                                   choices=METODO_PAGO_CHOICES,
                                   default= 'tarjeta')
    estado_de_pago = models.BooleanField(default=False)

    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='reserva_pasajero')  # Relación ManyToOne
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='vuelo_reserva')  # Relación ManyToOne


# Modelo Asiento (para Vuelo)
class Asiento(models.Model):
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

    lugar = [
        ("P", "Pasillo"),
        ("M", "Medio"),
        ("V", "Ventana")
    ]

    clase = models.CharField(max_length=1,choices=tipos_clase_avion,default='E')
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    posicion = models.CharField(max_length=1, choices=lugar)
    sistema_entretenimiento = models.BooleanField()

    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='asiento_vuelo')  # Relación ManyToOne
    pasajero = models.ForeignKey(Pasajero,on_delete=models.CASCADE, related_name='pajarelo_asiento')  # Relación ManyToOne 



# Modelo Servicio
class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=100)
    costo = models.FloatField()
    duracion_servicio = models.TimeField()
    añadido = models.CharField(max_length=100)

    aeropuerto = models.ManyToManyField(Aeropuerto, related_name='servicio_aeropuerto')  # Relación Many To Many

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
    
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE , related_name = 'empleado_servicio') #ManyToOne


    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.cargo}"
    


class Votacion(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=100)
    fecha_voto = models.DateTimeField(default=timezone.now)

    pasajero = models.ForeignKey(Pasajero , on_delete=models.CASCADE , related_name = 'voto_pasajero')
    aeropuerto = models.ForeignKey(Aeropuerto , on_delete=models.CASCADE , related_name = 'voto_aeropuerto')


class Banco(models.Model):
    Sucursal = [
        ('C', 'CAIXA'),
        ('B', 'BBVA'),
        ('U', 'UNICAJA'),
        ('I', 'ING'),
    ]

    banco = models.CharField(max_length=1,choices=Sucursal)
    pasajero = models.OneToOneField(Pasajero , on_delete=models.CASCADE , related_name = 'banco_pasajero')