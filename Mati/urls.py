from django.urls import path
from Mati.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("profes/", profesor, name="profesores"),
    path("estudiantes/", estudiante, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
    path("listacursos/", listar_cursos),
]