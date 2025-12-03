from django.http import HttpResponse
from django.shortcuts import render

def contacto(request):
    return render(request, "inicio/contacto.html")
    
def formulario(request):
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render(request, "inicio/ejemplo.html")

def registros (request):
    return render(request), "registros/principal.html"
