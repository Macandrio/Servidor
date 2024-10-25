from django.shortcuts import render
from .models import (
    Usuario,Proyecto,Tarea,
    AsignacionTarea,Etiqueta,Comentario
)

# Create your views here.
def index(request):
    return render(request, 'index.html') 

# 2. Una url que me muestre información sobre cada Proyectos
def dame_proyecto(request):
    proyecto = Proyecto.objects.select_related("creador").prefetch_related("colaboradores")
    proyecto = proyecto.all()

    return render(request, 'Proyecto/proyecto.html',{"dame_proyecto":proyecto})

# 3. Obtener las tareas asociadas al proyecto, ordenadas por fecha de creación descendente
def tareas_por_proyecto(request, proyecto_id):
    tareas = Tarea.objects.filter(proyecto=proyecto_id).select_related("proyecto").order_by('-fecha_creacion').all()
    return render(request, 'Proyecto/tarea_por_proyecto.html', {'tareas': tareas})

# 4. Obtener todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente
def asignacion_tarea(request, tarea_id):
    asignaciontarea = AsignacionTarea.objects.filter(tarea = tarea_id).select_related("usuario").select_related("tarea").order_by('fecha_asignacion').all()
    return render(request, 'Asignacion/asignacion_tarea.html', {'asignaciontarea': asignaciontarea})

# 5. todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.
def texto_observaciones(request,texto_observaciones):
    asignaciontarea = AsignacionTarea.objects.filter(observaciones__icontains = texto_observaciones).select_related("tarea").select_related("usuario").all()
    return render(request, 'Asignacion/texto_observacion.html', {'asignaciontarea': asignaciontarea})

# 6. Obtener Todos las tareas que se han creado entre dos años y el estado sea “Completada”.
def tarea_completada(request,fecha_inicio,fecha_final):
    tareas = Tarea.objects.filter(estado = "Co",
                                 fecha_creacion__year__gte = fecha_inicio,
                                 fecha_creacion__year__lte = fecha_final).select_related("proyecto").all()
    return render(request, 'Tarea/tarea_completada.html', {'tareas': tareas})

# 7. Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
def usuario_comentario(request):
    usuario = Usuario.objects.select_related("comentario")
    usuario = Usuario.objects.order_by("-comentario__fecha_comentario")[:1].get()