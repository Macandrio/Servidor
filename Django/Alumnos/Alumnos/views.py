
from django.shortcuts import render
from .models import *

def lista_usuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'lista_usuario.html', {'usuario_mostrar': usuario})

def lista_tarea(request):
    tarea = Tarea.objects.all()
    return render(request, 'lista_tarea.html', {'tarea_mostrar': tarea})

def lista_proyecto(request):
    proyecto = Proyecto.objects.all()
    return render(request, 'lista_proyecto.html', {'proyecto_mostrar': proyecto})

def lista_etiqueta(request):
    etiqueta = Etiqueta.objects.all()
    return render(request, 'lista_etiqueta.html', {'etiqueta_mostrar' : etiqueta})

def lista_comentario(request):
    comentario = Comentario.objects.all()
    return render(request, 'lista_comentario.html', {'comentario_mostrar' : comentario})

def lista_comentario(request):
    comentario = Comentario.objects.all()
    return render(request, 'lista_comentario.html', {'comentario_mostrar' : comentario})

#def lista_asignacion_de_tarea(request):
#    asignacion = AsignacionTarea.objects.all()
#    return render(request, 'lista_asignacion.html', {'asignacion_mostrar' : asignacion})