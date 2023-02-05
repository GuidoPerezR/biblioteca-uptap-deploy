from django.urls import path
from .views import *

app_name='modulo'
urlpatterns = [
    path('', ValidarInicioSesionAlumno, name="index"),
    path('BooksPage/', booksPage, name='BooksPage'),
    path('BookDetail/', bookDetail, name='BookDetail'),
    path('BookRequest/', bookRequest, name='BookRequest'),
    path('BookCart/', bookCart, name='BookCart'),
    
] 