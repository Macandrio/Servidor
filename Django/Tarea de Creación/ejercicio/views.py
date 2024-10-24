from django.shortcuts import render
from .models import (
    Usuario,Proyecto,Tarea,
    AsignacionTarea,Etiqueta,Comentario
)

# Create your views here.
def index(request):
    return render(request, 'index.html') 

#Una url que me muestre información sobre cada Proyectos
def dame_proyecto(request):
    proyecto = Proyecto.objects.select_related("creador").prefetch_related("colaboradores")
    proyecto = proyecto.all()

    return render(request, 'Proyecto/proyecto.html',{"dame_proyecto":proyecto})

# Obtener las tareas asociadas al proyecto, ordenadas por fecha de creación descendente
def tareas_por_proyecto(request, proyecto_id):
    tareas = Tarea.objects.filter(proyecto=proyecto_id).select_related("proyecto").order_by('-fecha_creacion')
    return render(request, 'Proyecto/tarea_por_proyecto.html', {'tareas': tareas})

#Obtener todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente
def asignacion_tarea(request, tarea_id):
    asignaciontarea = AsignacionTarea.objects.filter(tarea = tarea_id).select_related("usuario").select_related("tarea").order_by('fecha_asignacion')
    return render(request, 'Asignacion/asignacion_tarea.html', {'asignaciontarea': asignaciontarea})

#todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.
def texto_observaciones(request,texto_observaciones):
    asignaciontarea = AsignacionTarea.objects.filter(observaciones = texto_observaciones).select_related("tarea").select_related("usuario")
    return render(request, 'Asignacion/texto_observacion.html', {'asignaciontarea': asignaciontarea})