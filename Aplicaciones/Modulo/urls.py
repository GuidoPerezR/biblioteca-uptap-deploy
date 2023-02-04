from django.urls import path
from .views import *

app_name='modulo'
urlpatterns = [
    path('', ValidarInicioSesionAlumno, name="index"),
    path('BookDetail/', bookDetail, name='BookDetail'),
    path('BookDetail/BookRequest/', bookRequest, name='BookRequest'),
] 