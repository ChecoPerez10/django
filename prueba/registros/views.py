from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla de alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})
#indicamos el lugar donde se renderizara el dresultado de esta vista

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#Si los datos recibidos son correctos
            form.save()#inserta
            return redirect('Comentario')
    form= ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})

def contacto(request):
    return render(request,"registros/contacto.html")


def comentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/comentario.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id, 
    confirmacion='registros/confimarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/comentario.html", {'comentarios': comentarios})

    return render(request, confirmacion, {'object': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == 'POST':
        comentario.usuario = request.POST.get('usuario')
        comentario.mensaje = request.POST.get('mensaje')
        comentario.save()
        return redirect('Comentario')

    return render(request, 'registros/editarComentario.html', {'comentario': comentario})

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