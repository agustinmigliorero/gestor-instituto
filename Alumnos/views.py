from django.shortcuts import render
from django.http import HttpResponse
from Cursos.models import Alumno, Curso


def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return HttpResponse(alumnos)


def verAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    cursos = ""
    for curso in Curso.objects.all():
        if id_alumno in [al.id for al in curso.alumnos.all()]:
            cursos += f"{curso}<br>"
    context = {"alumno": alumno}
    return HttpResponse(cursos)


# Create your views here.
