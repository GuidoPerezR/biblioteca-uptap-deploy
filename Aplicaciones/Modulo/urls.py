from django.urls import path
from .views import *

app_name='modulo'
urlpatterns = [
    path('', ValidarInicioSesionUsuario, name="index"),
    path('BooksPage/', booksPage, name='BooksPage'),
    path('BookDetail/', bookDetail, name='BookDetail'),
    path('BookRequest/', bookRequest, name='BookRequest'),
    path('Adminn/', adminView, name='AdminBooksPage'),
    path('Adminnn/', adminView2, name='AdminBooksPage2'),
] 