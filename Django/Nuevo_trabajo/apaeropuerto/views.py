from django.shortcuts import render
import requests
from django.core import serializers



def index(request):
    return render(request, 'index.html')


def aeropuerto_listar_api(request):
    headers = {'Authorization': 'Bearer K7pmCsYBT0EPNIT3N8OdkLYOBR7rhj'}
    response = requests.get('http://127.0.0.1:8081/api/v1/Aeropuerto')

    aeropuertos = response.json()
    return render(request, 'paginas/aeropuerto_list.html', {"aeropuertos":aeropuertos})