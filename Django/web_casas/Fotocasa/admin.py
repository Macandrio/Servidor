from django.contrib import admin

# Register your models here.
from .models import Casa , Vendedor , Comprador
admin.site.register(Casa)
admin.site.register(Vendedor)
admin.site.register(Comprador)