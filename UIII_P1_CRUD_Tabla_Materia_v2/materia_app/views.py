from django.shortcuts import render, redirect
from .models import Materia

# Create your views here.

def Inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request, 'gestionarmateria.html', {'mismaterias' : lasmaterias})

def RegistrarMateria(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']

    guardarmaterias=Materia.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect ('/')