from django.urls import path
from materia_app import views

urlpatterns = [
    path('', views.Inicio_vista, name='Inicio_vista')
]