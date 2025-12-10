from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registros/contacto.html')
    form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})


def contacto(request):
    return render(request, "registros/contacto.html")


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {
        'comentarios': comentarios
    })


@permission_required('registros.delete_comentariocontacto', raise_exception=True)
def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultarComentario.html", {
            'comentarios': comentarios
        })
    return render(request, confirmacion, {
        'object': comentario
    })


@permission_required('registros.change_comentariocontacto', raise_exception=True)
def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultarComentario.html", {
                'comentarios': comentarios
            })

    form = ComentarioContactoForm(instance=comentario)
    return render(request, "registros/formEditarComentario.html", {
        'comentario': comentario,
        'form': form
    })


def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    return render(request, "registros/formEditarComentario.html", {
        'comentario': comentario,
        'form': ComentarioContactoForm(instance=comentario)
    })

def consulta1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta6(request):
    fechaInicio=datetime.date(2025,11,24)
    fechaFin=datetime.date(2025,11,27)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta8(request):
    inicio=datetime.date(2025,11,20)
    fin=datetime.date(2025,11,26)
    comentario=ComentarioContacto.objects.filter(created__range=(inicio,fin))
    return render(request,"registros/comentario.html",{'comentarios':comentario})

def consulta9(request, nombre):
    comentarios = ComentarioContacto.objects.filter(alumno__nombre__iexact=nombre)
    return render(request, "comentario/comentarios.html", {"comentarios": comentarios})

def consulta10(request):
    comentario=ComentarioContacto.objects.filter(mensaje__endswith ="o")
    return render(request,"registros/comentario.html",{'comentarios':comentario})


def consulta11(request):
    comentario=ComentarioContacto.objects.all().only("mensaje")
    return render(request,"registros/comentario.html",{'comentarios':comentario})

def consulta12(request):
    comentario=ComentarioContacto.objects.filter(mensaje__startswith="T")
    return render(request, "registros/comentario.html",{'comentarios':comentario})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id,matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})
#baby vamo a hacerlo como antes 

