from django.shortcuts import render, redirect
from django.db.models import Prefetch, Q, Sum, Count
from .models import (
    Aeropuerto, Vuelo, Pasajero, Equipaje, Aerolinea, 
    VueloAerolinea, Reserva, Empleado, Asiento, Servicio ,ContactoAeropuerto , EstadisticasVuelo , PerfilPasajero
)
from .forms import * # El * Coge todos los modelos es lo mismo que hacer lo de from .models import
from django.contrib import messages

def index(request):
    return render(request, 'index.html') 

#--------------------------------------------- Listas -----------------------------------------------------------------

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

#--------------------------------------------- Consultas -----------------------------------------------------------------


# 1. Todos los pasajeros que esten asociados a un vuelo con una relación reversa
def pasajeros_vuelo(request , id_vuelo):
    vuelo = Vuelo.objects.prefetch_related(Prefetch('vuelo_pasajero')).get(id=id_vuelo)
  
    return render(request, 'consultas/pasajeros_vuelo.html',{'vuelo': vuelo})
                         
# 2. Todos los vuelos que esten volando que esten una año en concreto

def vuelo_volando_año(request , anyo):
    datosvuelo = EstadisticasVuelo.objects.select_related('vuelo')
    datosvuelo = datosvuelo.filter(fecha_estadisticas__year = anyo, vuelo__estado = False)

    return render(request, 'consultas/vuelo_volando_año.html',{'datosvuelo': datosvuelo})

# 3. feedbacks de todos los vuelos que tenga una palabra en concreto de una aerolinea en concreto desde la tabla intermedia

def texto_vuelo_aerolinea(request, id_aerolinea, texto_buscar):
    
    aerolinea = Aerolinea.objects.get(id=id_aerolinea)

    vuelo_aerolinea = VueloAerolinea.objects.select_related('aerolinea','vuelo', 'vuelo__vuelo_datos')
    vuelo_aerolinea = vuelo_aerolinea.filter(aerolinea_id=id_aerolinea, vuelo__vuelo_datos__feedback_pasajeros__icontains=texto_buscar)
    return render(request, 'consultas/texto_vuelo_aerolinea.html', {'vuelo_aerolinea': vuelo_aerolinea, 'aerolinea': aerolinea})



# 4. Obtener el feedbacks de todos los vuelos en el que ha estado un pasajero específico.

def historial_feedbacks_pasajero(request, pasajero_id):

    pasajero = Pasajero.objects.get(id=pasajero_id) # Obtener el pasajero

    feedbacks = EstadisticasVuelo.objects.select_related('vuelo')
    feedbacks = feedbacks.filter(vuelo__vuelo_pasajero=pasajero)
    return render(request, 'consultas/historial_feedbacks_pasajero.html', {'feedbacks': feedbacks, 'pasajero': pasajero})


#5. Obtener todos los vuelos que salgan desde un aeropuerto específico y lleguen a un destino específico

def vuelos_origen_destino(request, origen_id, destino_id):
    
    vuelos = Vuelo.objects.select_related('origen', 'destino') 
    vuelos = vuelos.filter(origen_id=origen_id, destino_id=destino_id)

    return render(request, 'consultas/vuelos_origen_destino.html', {'vuelos': vuelos})


#6. Listar reservas por método de pago y año

def reservas_por_metodo_y_año(request, metodo_pago, año):
    reservas = Reserva.objects.select_related('pasajero', 'vuelo')
    reservas = reservas.filter(metodo_pago=metodo_pago,fecha_reserva__year=año)

    return render(request, 'consultas/reservas_por_metodo_y_año.html', {'reservas': reservas})


# 7. Obtener todos los vuelos que tengan un origen y destino en concreto o que el estado sea volando

def vuelos_cortos_origen_destino(request, origen_id, destino_id, estado):

    vuelos = Vuelo.objects.select_related('origen', 'destino')
    vuelos = vuelos.filter(Q(origen_id=origen_id) & Q(destino_id=destino_id) | (~Q(estado=estado)))

    return render(request, 'consultas/vuelos_cortos.html', {'vuelos': vuelos})



# 8. Calcular el peso total del equipaje de todos los pasajeros en un vuelo específico y ordenar
def peso_equipaje_vuelo(request, vuelo_id):
    
    equipajes = Equipaje.objects.select_related('pasajero')
    equipajes = equipajes.filter(pasajero__vuelo__id=vuelo_id).order_by('-peso')[:5] 
    peso_total = equipajes.aggregate(Sum('peso'))['peso__sum']  

    return render(request, 'consultas/peso_equipaje_vuelo.html', {'equipajes': equipajes,'peso_total': peso_total})

# 9. Listar todos los vuelos de una aerolínea específica que no tienen registrada una fecha de operación en la tabla intermedia
def vuelos_sin_operacion(request, aerolinea_id):

    vuelos = VueloAerolinea.objects.select_related('aerolinea', 'vuelo')
    vuelos = vuelos.filter(aerolinea_id=aerolinea_id, fecha_operacion__isnull=True)

    return render(request, 'consultas/vuelos_sin_operacion.html', {'vuelos': vuelos})



# 10. Calcular cuantos pasajeros hay en un vuelo
def cuantos_pasajeros_vuelo(request, id_vuelo):
    
    pasajeros = Pasajero.objects.prefetch_related('vuelo')
    pasajeros = pasajeros.filter(vuelo__id=id_vuelo)
    total_pasajeros = pasajeros.aggregate(Count('id'))['id__count']
    
    return render(request, 'consultas/total_pasajeros.html', {'total_pasajeros': total_pasajeros, 'pasajeros': pasajeros})

#----------------------------------------------------------------------- Formulario -----------------------------------------------------------------

# Formulario Aeropuerto

def crear_aeropuerto(request):
    if request.method == "POST":
        formulario = AeropuertoForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "El aeropuerto se creó exitosamente.")
                return redirect("lista_aeropuerto")
            except Exception as error:
                messages.error(request, f"Error inesperado al guardar el aeropuerto: {error}")
        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, "Ya existe un aeropuerto con el mismo nombre. Verifica los datos ingresados.")
    else:
        formulario = AeropuertoForm()

    return render(request, 'Formularios/Aeropuerto/crear_aeropuerto.html', {"formulario": formulario})

def Aeropuerto_buscar_avanzado(request):
    if len(request.GET) > 0:
        formulario = BusquedaAvanzadaAeropuertoForm(request.GET)
        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes valores:\n"
            
            # Obtener el QuerySet base
            QSaeropuertos = Aeropuerto.objects.prefetch_related(
                Prefetch('aerolinea_de_aeropuerto'),  # ManyToMany con Aerolínea
                Prefetch('vuelos_de_origen'),         # ManyToOne reversa con Vuelo (origen)
                Prefetch('vuelos_de_destino'),        # ManyToOne reversa con Vuelo (destino)
                Prefetch('servicio_aeropuerto')       # ManyToMany con Servicio
            )
            
            # Obtener los filtros
            textoBusqueda = formulario.cleaned_data.get('textoBusqueda')
            ciudades = formulario.cleaned_data.get('ciudad')
            
            # Filtro por texto de búsqueda
            if textoBusqueda:
                QSaeropuertos = QSaeropuertos.filter(nombre__icontains=textoBusqueda)
                mensaje_busqueda += f"Nombre que contiene la palabra '{textoBusqueda}'\n"
            
            # Filtro por ciudades
            if ciudades:
                mensaje_busqueda += f"Ciudad que sea: {', '.join(ciudades)}\n"
                filtro_ciudades = Q(ciudades=ciudades[0])
                for ciudad in ciudades[1:]:
                    filtro_ciudades |= Q(ciudades=ciudad)
                QSaeropuertos = QSaeropuertos.filter(filtro_ciudades)
            
            aeropuertos = QSaeropuertos.all()
            
            return render(
                request,
                'Formularios/Aeropuerto/lista_busqueda.html',
                {"aeropuertos_mostrar": aeropuertos, "texto_busqueda": mensaje_busqueda}
            )
    else:
        formulario = BusquedaAvanzadaAeropuertoForm()
    return render(
        request,
        'Formularios/Aeropuerto/busqueda_avanzada.html',
        {"formulario": formulario}
    )

def editar_aeropuerto(request, id):
    aeropuerto = Aeropuerto.objects.get(id=id)  # Obtiene el aeropuerto por ID
    if request.method == 'POST':
        formulario = AeropuertoForm(request.POST, instance=aeropuerto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aeropuerto')  # Redirige a la lista después de actualizar
    else:
        formulario = AeropuertoForm(instance=aeropuerto)

    return render(request, 'Formulario/Aeropuerto/editar_aeropuerto.html', {'formulario': formulario, 'aeropuerto': aeropuerto})

def eliminar_aeropuerto(request, id):
    aeropuerto = Aeropuerto.objects.get(id=id)
    if request.method == 'POST':
        aeropuerto.delete()
        return redirect('lista_aeropuerto')  # Redirige a la lista después de eliminar
    return render(request, 'Formulario/Aeropuerto/eliminar_aeropuerto.html', {'aeropuerto': aeropuerto})

  
    
# Formulario contacto_Aeropuerto

def crear_contacto(request): 
    if (request.method == "POST"):
        formulario=ContactoAeropuertoform(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "El contacto se creó exitosamente.")
                return redirect("lista_ContactoAeropuerto")
            except Exception as error:
                print(error)
    else:
        formulario=ContactoAeropuertoform()  
    return render(request,'Formularios/Contacto_Aeropuerto/crear_Contacto.html',{"formulario":formulario})


# Formulario estadisticasvuelo

def crear_estadisticasvuelo(request): 
    if (request.method == "POST"):
        formulario=estadisticasvueloform(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "La Estasdistica se creó exitosamente.")
                return redirect("lista_EstadisticasVuelo")
            except Exception as error:
                print(error)
    else:
        formulario=estadisticasvueloform()  
    return render(request,'Formularios/Estadisticas_vuelo/crear_Estadisticasvuelo.html',{"formulario":formulario})

# Formulario Aerolinea

def crear_Aerolinea(request): 
    if (request.method == "POST"):
        formulario=Aerolineaform(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "La Aerolinea se creó exitosamente.")
                return redirect("lista_aerolineas")
            except Exception as error:
                print(error)
    else:
        formulario=Aerolineaform()  
    return render(request,'Formularios/Aerolinea/crear_aerolinea.html',{"formulario":formulario})

# Formulario Vuelo

def crear_Vuelo(request): 
    if (request.method == "POST"):
        formulario=VueloForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.success(request, "El vuelo se creó exitosamente.")
                return redirect("lista_vuelo")
            except Exception as error:
                print(error)
    else:
        formulario=VueloForm()  
    return render(request,'Formularios/Vuelo/crear_vuelo.html',{"formulario":formulario})

#Formulario Pasajero

def crear_pasajero(request): 
    if (request.method == "POST"):
        formulario=PasajeroForm(request.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                return redirect("lista_pasajero")
            except Exception as error:
                print(error)
    else:
        formulario=PasajeroForm    
    return render(request,'Formularios/Pasajero/crear_pasajero.html',{"formulario":formulario})

#--------------------------------------------- Errores -----------------------------------------------------------------

# Error 400 - Solicitud Incorrecta
def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

# Error 403 - Prohibido
def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)

# Error 404 - No Encontrado
def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

# Error 500 - Error Interno del Servidor
def error_500(request):
    return render(request, 'errors/500.html', status=500)





