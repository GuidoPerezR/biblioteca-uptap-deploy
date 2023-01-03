from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Libro)
admin.site.register(Cargo)
admin.site.register(Docente_administrativo)
admin.site.register(Administrador)
admin.site.register(Usuario)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    ordering = ('matricula',)
    search_fields = ('id_carrera', 'id_cuatrimestre',)
    #exclude = ('matricula',)

@admin.register(Cuatrimestre)
class CuatrimestreAdmin(admin.ModelAdmin):
    ordering = ('nombre_cuatrimestre',)
    search_fields = ('nombre_cuatrimestre',)
    exclude = ('id_cuatrimestre',)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    ordering = ('nom_carrera',)
    search_fields = ('nom_carrera',)
    exclude = ('id_carrera',)