from django.urls import path
from . import views

urlpatterns = [
    path('Animales/', views.listar_Animales, name='listar_animales'),
    path('Protectoras/', views.listar_Protectoras, name='listar_protectoras'),
    path('Colaboradores/', views.listar_Colaboradores, name='listar_colaboradores'),
]
