from django.shortcuts import render
from django.http import HttpResponse
from Mati.models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request,"index.html")

def estudiante(request):
    estudiantes=Estudiante.objects.all()
    if request.method=="POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            estudiante=Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            form=EstudianteForm()
            return render(request,"estudiantes.html", {"formulario":form, "estudiantes":estudiantes, "mensaje":"Estudiante creado"})
        else:
            return render(request,"estudiantes.html", {"formulario":form, "estudiantes":estudiantes, "mensaje":"Datos inválidos"})    
    else:
        form=EstudianteForm()
        return render(request,"estudiantes.html", {"formulario":form, "estudiantes":estudiantes})

def profesor(request):
    profes=Profesor.objects.all()
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profe=Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
            profe.save()
            form=ProfesorForm()
            return render(request,"profesores.html", {"formulario":form, "profesores":profes, "mensaje":"Profesor creado"})
        else:
            return render(request,"profesores.html", {"formulario":form, "profesores":profes, "mensaje":"Datos inválidos"})
    else:
        form=ProfesorForm()
        return render(request,"profesores.html", {"formulario":form, "profesores":profes})

def cursos(request):
    cursos=Curso.objects.all()
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            form=CursoForm()
            return render(request, "cursos.html", {"formulario":form, "cursos":cursos, "mensaje":"Curso creado"})
        return render(request, "cursos.html", {"formulario":form, "cursos":cursos, "mensaje":"Datos inválidos"})
    else:
        form=CursoForm()
        return render(request, "cursos.html", {"formulario":form, "cursos":cursos})

def listar_profes(request):
    profes=Profesor.objects.all()
    respuesta=""
    for profe in profes:
        respuesta+=f"{profe.nombre} {profe.apellido} - {profe.profesion}"
    return HttpResponse(respuesta)   

def listar_estudiantes(request):
    estudiantes=Estudiante.objects.all()
    respuesta=""
    for estudiante in estudiantes:
        respuesta+=f"{estudiante.nombre} {estudiante.apellido}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos=Curso.objects.all()
    respuesta=""
    for curso in cursos:
        respuesta+=f"{curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)