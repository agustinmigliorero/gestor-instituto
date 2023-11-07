from django.contrib import admin
from .models import Curso, Alumno, Instructor


class filtrarAlumnos(admin.ModelAdmin):
    filter_horizontal = ("alumnos",)


admin.site.register(Curso, filtrarAlumnos)
admin.site.register(Alumno)
admin.site.register(Instructor)

# Register your models here.
