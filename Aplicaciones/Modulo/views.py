from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def ValidarInicioSesionAlumno(request):
    if request.method=='POST':
        try:
            detalleAlumno=Alumno.objects.get(email=request.POST['email'], contraseña=request.POST['contraseña'])
            request.session['email']=detalleAlumno.email
            return render(request, "paginaLibros.html")
            
        except Alumno.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
    return render(request, "logIn.html")

def bookDetail(request):
    return render(request, "bookDetail.html")