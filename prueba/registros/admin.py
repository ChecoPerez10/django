from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    # Siempre deben ser solo lectura
    readonly_fields = ('created', 'updated')

    list_display = ('matricula', 'nombre', 'carrera', 'turno','created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    # Solo bloquear campos al EDITAR, no al CREAR
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si está editando
            return ('created', 'updated', 'matricula')
        else:    # Si está creando
            return ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ("id", "coment")
    search_fields = ("id", "created")
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
