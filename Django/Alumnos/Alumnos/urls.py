from django.urls import path
from . import views

urlpatterns = [
    path('Usuario/', views.lista_usuario,name='lista_usuario'),
    path('Tarea/', views.lista_tarea,name='lista_tarea'),
    path('Proyecto/', views.lista_proyecto,name='lista_proyecto'),
    path('Etiqueta/', views.lista_etiqueta,name='lista_etiqueta'),
    #path('Asignacion_de_tarea/', views.lista_asignacion_de_tarea,name='lista_asignacion_de_tarea'),
    path('Comentario/', views.lista_comentario,name='lista_comentario'),

]