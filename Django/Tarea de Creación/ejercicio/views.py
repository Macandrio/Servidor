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