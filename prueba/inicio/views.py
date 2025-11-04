from django.http import HttpResponse
from django.shortcuts import render

def contacto(request):
    return render(request, "inicio/contacto.html")
    
def registrar(request):
    return render(request, "inicio/formulario.html")

def principal(request):
    return render(request, "inicio/principal.html")

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")