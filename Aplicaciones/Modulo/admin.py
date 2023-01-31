from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Libro)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    ordering = ('matricula',)
    search_fields = ('id_carrera', 'id_cuatrimestre',)
    #exclude = ('matricula',)

@admin.register(Cuatrimestre)
class CuatrimestreAdmin(admin.ModelAdmin):
    ordering = ('nombre_cuatrimestre',)
    search_fields = ('nombre_cuatrimestre',)
    exclude = ('id_cuatrimestre', 'nombre_cuatrimestre')

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    ordering = ('nom_carrera',)
    search_fields = ('nom_carrera',)
    exclude = ('id_carrera', 'nom_carrera')
