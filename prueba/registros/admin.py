from django.contrib import admin
from .models import Alumnos

admin.site.register(Alumnos)

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','update')


