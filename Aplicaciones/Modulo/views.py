from django.shortcuts import render, redirect
#from .forms import ProductForm
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def ValidarInicioSesionAlumno(request):
    if request.method=='POST':
        try:
            detalleAlumno=Alumno.objects.get(email=request.POST['email'], contraseña=request.POST['contraseña'])
            request.session['email']=detalleAlumno.email
            return redirect('BooksPage/')
            
        except Alumno.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
    return render(request, "logIn.html")

def bookDetail(request):
    return render(request, "bookDetail.html")

@login_required 
def bookRequest(request):
    return render(request, "bookRequest.html")

@login_required 
def booksPage(request):
    return render(request, "paginaLibros.html")

def bookCart(request):
    return render(request, "bookCart.html")

def userMenu(request):
    return render(request, "userMenu.html")