from django.shortcuts import render
from .models import (
    Aeropuerto, Vuelo, Pasajero, Equipaje, Aerolinea, 
    VueloAerolinea, Reserva, Empleado, Asiento, Servicio ,ContactoAeropuerto , EstadisticasVuelo , PerfilPasajero
)

def index(request):
    return render(request, 'index.html') 

# Vista para listar Aeropuertos
def lista_aeropuerto(request):
    aeropuertos = Aeropuerto.objects.all()
    return render(request, 'paginas/aeropuerto_list.html', {'aeropuertos': aeropuertos})

# Vista para listar Vuelos
def lista_vuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'paginas/vuelo_list.html', {'vuelos': vuelos})

# Vista para listar Pasajeros
def lista_pasajero(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'paginas/pasajero_list.html', {'pasajeros': pasajeros})

# Vista para listar Equipajes
def lista_equipaje(request):
    equipajes = Equipaje.objects.all()
    return render(request, 'paginas/equipaje_list.html', {'equipajes': equipajes})

# Vista para listar Aerolíneas
def lista_aerolineas(request):  # Cambiado aquí
    aerolineas = Aerolinea.objects.all()
    return render(request, 'paginas/aerolinea_list.html', {'aerolineas': aerolineas})

# Vista para listar VueloAerolinea
def lista_vuelos_aerolineas(request):  # Cambiado aquí
    vuelos_aerolineas = VueloAerolinea.objects.all()
    return render(request, 'paginas/vuelo_aerolinea_list.html', {'vuelos_aerolineas': vuelos_aerolineas})

# Vista para listar Reservas
def lista_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'paginas/reserva_list.html', {'reservas': reservas})

# Vista para listar Empleados
def lista_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'paginas/empleado_list.html', {'empleados': empleados})

# Vista para listar Asientos
def lista_silla(request):
    sillas = Asiento.objects.all()
    return render(request, 'paginas/silla_list.html', {'sillas': sillas})

# Vista para listar Servicios
def lista_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'paginas/servicio_list.html', {'servicios': servicios})

# Vista para listar ContactoAeropuerto
def lista_ContactoAeropuerto(request):
    contactoAero = ContactoAeropuerto.objects.all()
    return render(request, 'paginas/lista_ContactoAeropuerto_listar.html', {'contactoAero': contactoAero})

# Vista para listar EstadisticasVuelo
def lista_EstadisticasVuelo(request):
    estadisticas = EstadisticasVuelo.objects.all()
    return render(request, 'paginas/estadisticas_list.html', {'estadisticas': estadisticas})

# Vista para listar PerfilPasajero
def lista_PerfilPasajero(request):
    perfilpasajero = PerfilPasajero.objects.all()
    return render(request, 'paginas/perfilpasajero_list.html', {'perfilpasajero': perfilpasajero})


