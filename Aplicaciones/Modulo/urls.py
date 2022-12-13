from django.urls import path
from .views import *

app_name='modulo'
urlpatterns = [
    path('', Modulo, name="index"),
    path('IniciarSesion/', ValidarInicioSesionAlumno, name='IniciarSesion'),
    path('IniciarSesionProfAsig', IniciarSesionProfAsig),
    path('IniciarSesionProfTC', IniciarSesionProfTC),
    path('PaginaLibros/', PaginaLibros, name='paginaLibros'),
    #path('IniciarSesion/PaginaLibros/', PaginaLibros, name='paginaLibros'),
    #path('IniciarSesion/Registro/', Registro, name='registro'),
    path('IniciarSesion/FormularioRegistro/', FormularioRegistro, name='FormularioRegistro'),
    path('IniciarSesion/Registro/IniciarSesion', IniciarSesion),
    path('IniciarSesion/Registro/IniciarSesion/PaginaLibros', PaginaLibros)
] 