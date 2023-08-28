from django.contrib import admin
from .models import Curso, Profesor, Estudiante

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)