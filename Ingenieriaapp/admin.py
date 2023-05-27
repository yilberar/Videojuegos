from django.contrib import admin
from .models import Usuario, Videojuegos, Solicitud

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Videojuegos)
admin.site.register(Solicitud)