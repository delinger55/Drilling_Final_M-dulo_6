from django.contrib import admin
from .models import Vehiculo


#class VehiculoAdmin(UserAdmin):
#   model = Vehiculo
#   list_display = ['marca', 'modelo', 'precio', 'fecha_creacion', 'fecha_modificacion']

admin.site.register(Vehiculo)#VehiculoAdmin

