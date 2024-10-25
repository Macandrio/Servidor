from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path("proyecto/", views.dame_proyecto,name="dame_proyecto"),
    path('proyectos/<int:proyecto_id>/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Tareas por proyecto
    path('usuario/tareas/', views.tareas_por_proyecto, name='tareas_por_proyecto'),  # Usuarios tarea asignadas
    path('asignaciones/<int:tarea_id>/', views.asignacion_tarea, name='asignacion_tarea'),  # URL para obtener asignaciones por tarea
    path("asignaciones/<str:texto_observaciones>/tarea", views.texto_observaciones,name="texto_observaciones"),
    path("tarea/proyecto/<int:fecha_inicio>/<int:fecha_final>", views.tarea_completada,name="tarea_completada"),
    path("usuario/comentario/<int:proyecto_id>", views.usuario_comentario,name="usuario_comentario"),

]