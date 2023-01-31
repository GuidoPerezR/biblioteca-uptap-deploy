from django.urls import path
from .views import *

app_name='modulo'
urlpatterns = [
    path('', ValidarInicioSesionAlumno, name="index"),
    path('PaginaLibros/', PaginaLibros, name='paginaLibros'),
] 