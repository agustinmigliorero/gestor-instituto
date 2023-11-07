from django.shortcuts import render
from .models import Curso


def index(request):
    cursos = Curso.objects.all()
    context = {
        "cursos": cursos,
    }
    return render(request, "index.html", context)


def verCurso(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    context = {"curso": curso}
    return render(request, "ver-curso.html", context)


# Create your views here.
