from django import forms

from .models import *

class ProductForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellidos = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=50, required=True)
    matricula = forms.IntegerField()
    carrera = forms.ModelChoiceField(label="Carrera", queryset=Carrera.objects.all())
    cuatrimestre = forms.ModelChoiceField(label="Cuatrimestre", queryset=Cuatrimestre.objects.all())
    turno = forms.CharField(max_length=50, required=True)
    contraseña = forms.CharField(max_length=50, required=True)