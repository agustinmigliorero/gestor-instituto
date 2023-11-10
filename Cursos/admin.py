from django.contrib import admin
from .models import Curso, Alumno, Instructor, AlumnoCursos


class AlumnoCursosInline(admin.TabularInline):
    model = AlumnoCursos
    extra = 1
    ordering = ["Alumno__apellido", "Alumno__nombre"]


class formAlumnos(admin.ModelAdmin):
    list_display = [
        "nombre",
        "apellido",
        "email",
        "fechaNacimiento",
        "documento",
        "Mostrar_Cantidad_Cursos",
    ]
    # filter_horizontal = ("cursos",)
    search_fields = ["nombre", "documento"]
    inlines = [
        AlumnoCursosInline,
    ]
    ordering = ["apellido", "nombre"]


class formCursos(admin.ModelAdmin):
    list_display = [
        "id",
        "nombre",
        "instructor",
        "fechaDeInicio",
        "fechaDeFinalizacion",
        "horario",
        "diasDeLaSemana",
        "Mostrar_Cantidad_Alumnos",
    ]
    filter_horizontal = ["alumnos"]
    search_fields = ["nombre", "id"]
    inlines = [
        AlumnoCursosInline,
    ]
    ordering = ["id", "nombre"]
    # model = Curso.alumnos.through


# class formAlumnosYCursos(admin.ModelAdmin):
#     # filter_horizontal = ["Alumno"]
#     []


admin.site.register(Curso, formCursos)
admin.site.register(Alumno, formAlumnos)
admin.site.register(Instructor)
# admin.site.register(AlumnoCursos)

# Register your models here.
