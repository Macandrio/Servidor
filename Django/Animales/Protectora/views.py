from django.shortcuts import render
from .models import *

# Create your views here.

def listar_Protectoras(request) :
    protectora = Protectora.objects.all()
    return render(request, 'protectora/protectora_list.html', {'Protectora_mostrar': protectora})

def listar_Colaboradores(request) :
    colaborador = Colaborador.objects.all()
    return render(request, 'colaboradores/colaborador_list.html', {'colaborador_mostrar': colaborador})

def listar_Animales(request) :
    animales = Animales.objects.all()
    return render(request, 'animales/animales_list.html', {'Animales_mostrar': animales})