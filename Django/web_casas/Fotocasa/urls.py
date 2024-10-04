from django.urls import path
from . import views

urlpatterns = [
    path('Casa/', views.listar_Casa, name='listar_Casa'),
    path('Comprador/', views.listar_Comprador, name='listar_Comprador'),
    path('Vendedor/', views.listar_Vendedor, name='listar_Vendedor'),
]
