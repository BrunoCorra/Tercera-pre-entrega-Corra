from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea

def saludo(request):
    return HttpResponse("hi world")

def mostrar_mis_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "hola_mundo/tareas.html", {"tareas": tareas})