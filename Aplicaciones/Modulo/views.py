from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ProductForm
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def Modulo(request):
    return render(request, "Modulos.html")

def IniciarSesion(request):
    return render(request, "IniciarSesion.html")

def IniciarSesionProfAsig(request):
    return render(request, "IniciarSesionProfAsig.html")

def IniciarSesionProfTC(request):
    return render(request, "IniciarSesionProfTC.html")

def PaginaLibros(request):
    return render(request, "paginaLibros.html")

def Registro(request):
    return render(request, "Registro.html")

def FormularioRegistro(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            messages.add_message(request=request, level=messages.SUCCESS, message="Te has registrado correctamente")

            alumno = Alumno()

            alumno.matricula = form.cleaned_data['matricula']
            alumno.nombre = form.cleaned_data['nombre']
            alumno.apellidos = form.cleaned_data['apellidos']
            alumno.turno = form.cleaned_data['turno']
            alumno.email = form.cleaned_data['email']
            alumno.id_carrera = form.cleaned_data['carrera']
            alumno.id_cuatrimestre = form.cleaned_data['cuatrimestre']
            alumno.contraseña = form.cleaned_data['contraseña']

            alumno.save()
            
            return redirect('modulo:IniciarSesion')
        else:
            print("Invalido")


    return render(request, 'Registro.html', {'form':form})

def ValidarInicioSesionAlumno(request):
    if request.method=='POST':
        try:
            detalleAlumno=Alumno.objects.get(email=request.POST['email'], contraseña=request.POST['contraseña'])
            request.session['email']=detalleAlumno.email
            return render(request, "paginaLibros.html")
        except Alumno.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
    return render(request, "IniciarSesion.html")

#class FormularioRegistro(HttpRequest):

    def index(request):
        alumno = Registro()
        return render(request, 'Registro.html', {"form": alumno})

    def procesar_formulariio(request):
        alumno = Registro()
        if alumno.is_valid():
            alumno.save()
            alumno = Registro()

        return render(request, "Registro.html", {"form":alumno, "mensaje":'OK'})