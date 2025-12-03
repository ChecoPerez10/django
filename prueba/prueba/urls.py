from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inicio import views as views_inicio
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name='Principal'),
    path('contacto/', views_registros.contacto, name='Contacto'),
    path('formulario/', views_registros.registrar, name="Formulario"),
    path('ejemplo/', views_inicio.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultarComentario/',  views_registros.consultarComentario,  name="ConsultarComentario"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',  views_registros.editarComentarioContacto, name='Editar'),
    path('consultas1', views_registros.consultar1, name="Consultas1"),
    path('consultas2', views_registros.consultar2, name="Consultas2"),
    path('consultas3', views_registros.consultar3, name="Consultas3"),
    path('consultas4', views_registros.consultar4, name="Consultas4"),
    path('consultas5', views_registros.consultar5, name="Consultas5"),
    path('consultas6', views_registros.consultar6, name="Consultas6"),
    path('consultas7', views_registros.consultar7, name="Consultas7"),
    path('consultas8', views_registros.consultar8, name="Consultas8"),
    path('consultas9', views_registros.consultar9, name="Consultas9"),
    path('consultas10', views_registros.consultar10, name="Consultas10"),
    path('consultas11', views_registros.consultar11, name="Consultas11"),
    path('consultas12', views_registros.consultar12, name="Consultas12"),
    path('consultasSQL',views_registros.consultasSQL,name="sql"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
