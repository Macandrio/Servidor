from django.shortcuts import render
from .models import *

# Create your views here.

def listar_Casa(request) :
    casa = Casa.objects.all()
    return render(request, 'listar_Casa.html', {'Casa_mostrar': casa})

def listar_Vendedor(request) :
    vendedor = Vendedor.objects.all()
    return render(request, 'listar_Vendedor.html', {'Vendedor_mostrar': vendedor})

def listar_Comprador(request) :
    comprador = Comprador.objects.all()
    return render(request, 'listar_Comprador.html', {'Comprador_mostrar': comprador})

