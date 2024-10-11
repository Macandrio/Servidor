
from django.contrib import admin

# Register your models here.
from .models import Usuario
admin.site.register(Usuario)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Etiqueta
admin.site.register(Etiqueta)

from .models import Tarea
admin.site.register(Tarea)

from .models import AsignacionTarea
admin.site.register(AsignacionTarea)

from .models import Comentario
admin.site.register(Comentario)
