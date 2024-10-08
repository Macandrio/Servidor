from django.db import models
from django.utils import timezone

# Create your models here.

class Biblioteca (models.Model):
    nombre = models.CharField(max_length=100)
    direccion =models.TextField()

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200,blank=True)
    edad = models.IntegerField(null=True)
    
    
class Libro(models.Model):
    Idiomas = [
        ("ES", "ESPAÑOL"),
        ("EN", "INGLÉS"),
        ("FR", "FRANCÉS"),
        ("IT", "ITALIANO")
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=200,choices=Idiomas,default="ES")
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE)
    autores =   models.ManyToManyField(Autor)



class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    puntos = models.FloatField(default=5.8,db_column="puntos_biblioteca")

class DatosCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete = models.CASCADE)
    direccion = models.TextField()
    gustos = models.TextField() 
    telefono = models.IntegerField()

class Prestamos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE )
    fecha_prestamos = models.DateTimeField(default=timezone.now)

    
