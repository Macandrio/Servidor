from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),  # Página de inicio
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'), #Datos del proyecto
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Tareas por proyecto
    path('usuario/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Usuarios tarea asignadas
    path('asignaciones/<int:tarea_id>/', views.asignacion_tarea, name='asignacion_tarea'),  # URL para obtener asignaciones por tarea

    

]
