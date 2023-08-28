from django.urls import path
from Mati.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("arbitros/", arbitro, name="arbitros"),
    path("equipos/", equipo, name="equipos"),
    path("torneos/", torneo, name="torneos"),
    path("buscar/", busqueda, name="buscar"),
    path("resultados-torneo/", buscarTorneo, name="ResultadoTorneo"),
    path("resultados-equipo/", buscarEquipo, name="ResultadoEquipo"),
    path("resultados-arbitro/", buscarArbitro, name="ResultadoArbitro"),
    
]