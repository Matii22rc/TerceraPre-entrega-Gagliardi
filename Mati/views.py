from django.shortcuts import render
from django.http import HttpResponse
from Mati.models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request,"index.html")

def equipo(request):
    equipos=Equipo.objects.all()
    if request.method=="POST":
        form=EquipoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            jugadores=info["jugadores"]
            equipo=Equipo(nombre=nombre, jugadores=jugadores)
            equipo.save()
            form=EquipoForm()
            return render(request,"equipos.html", {"formulario":form, "equipos":equipos, "mensaje":"Equipo creado"})
        else:
            return render(request,"equipos.html", {"formulario":form, "equipos":equipos, "mensaje":"Datos inválidos"})    
    else:
        form=EquipoForm()
        return render(request,"equipos.html", {"formulario":form, "equipos":equipos})

def arbitro(request):
    arbitros=Arbitro.objects.all()
    if request.method=="POST":
        form=ArbitroForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            arbitro=Arbitro(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            arbitro.save()
            form=ArbitroForm()
            return render(request,"arbitros.html", {"formulario":form, "arbitros":arbitros, "mensaje":"Arbitro creado"})
        else:
            return render(request,"arbitros.html", {"formulario":form, "arbitros":arbitros, "mensaje":"Datos inválidos"})
    else:
        form=ArbitroForm()
        return render(request,"arbitros.html", {"formulario":form, "arbitros":arbitros})

def torneo(request):
    torneos=Torneo.objects.all()
    if request.method=="POST":
        form=TorneoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            torneo=Torneo(nombre=nombre)
            torneo.save()
            form=TorneoForm()
            return render(request, "torneos.html", {"formulario":form, "torneos":torneos, "mensaje":"Torneo creado"})
        return render(request, "torneos.html", {"formulario":form, "torneos":torneos, "mensaje":"Datos inválidos"})
    else:
        form=TorneoForm()
        return render(request, "torneos.html", {"formulario":form, "torneos":torneos})

def busqueda(request):
    return render(request, "busqueda.html")

def buscarTorneo(request):
    torneo=request.GET["torneo"]
    if torneo!="":
        torneos=Torneo.objects.filter(nombre__icontains=torneo)
        return render(request, "resultadosBusqueda-torneo.html", {"torneos":torneos})
    else:
        return render(request, "busqueda.html", {"mensaje":"Ningún dato ingresado"})

def buscarArbitro(request):
    arbitro=request.GET["arbitro"]
    if parbitro!="":
        arbitros=Arbitro.objects.filter(apellido=arbitro)
        return render(request, "resultadosBusqueda-arbitro.html", {"arbitros":arbitros})
    else:
        return render(request, "busqueda.html", {"mensaje":"Ningún dato ingresado"})

def buscarEquipo(request):
    equipo=request.GET["equipo"]
    if equipo!="":
        equipos=Equipo.objects.filter(nombre=equipo)
        return render(request, "resultadosBusqueda-equipo.html", {"equipos":equipos})
    else:
        return render(request, "busqueda.html", {"mensaje":"Ningún dato ingresado"})