from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aeropuerto/', views.aeropuerto_listar_api, name='aeropuerto_listar_api'),
]