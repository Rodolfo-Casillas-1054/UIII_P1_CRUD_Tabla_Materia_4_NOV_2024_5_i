from django.shortcuts import render
from .models import Materia

# Create your views here.

def Inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request, 'gestionarmateria.html')
