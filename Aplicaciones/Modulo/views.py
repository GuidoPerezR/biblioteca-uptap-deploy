from django.shortcuts import render, redirect
#from .forms import ProductForm
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def ValidarInicioSesionUsuario(request):
    if request.method=='POST':
        try:
            detalleUsuario=Usuario.objects.get(email=request.POST['email'], contraseña=request.POST['contraseña'])
            request.session['email']=detalleUsuario.email
            return redirect('BooksPage/')
            
        except Usuario.DoesNotExist as e:
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

def adminView(request):
    return render(request, "adminBooksPage.html")

def adminView2(request):
    return render(request, "adminAddUser.html")
