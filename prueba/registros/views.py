from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
import datetime

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

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI", turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar3(request):
    alumnos = Alumnos.objects.only("matricula", "nombre", "carrera", "turno")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__icontains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar6(request):
    fechaInicio = datetime.date(2025, 10, 28)
    fechaFin = datetime.date(2025, 10, 28)
    alumnos = Alumnos.objects.filter(created__date__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__icontains="No inscrito").distinct()
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar8(request):
    alumnos = Alumnos.objects.filter(nombre__startswith="A")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar9(request):
    alumnos = Alumnos.objects.filter(
        Q(turno="Matutino") | Q(turno="Vespertino")
    )
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar10(request):
    alumnos = Alumnos.objects.exclude(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar11(request):
    alumnos = Alumnos.objects.all().order_by("nombre")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar12(request):
    fechaInicio = datetime.date(2024, 1, 1)
    fechaFin = datetime.date(2024, 12, 31)
    alumnos = Alumnos.objects.filter(created__date__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen '
        'FROM registros_alumnos '
        'WHERE carrera = "TI" '
        'ORDER BY turno DESC')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})




