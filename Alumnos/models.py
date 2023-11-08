from django.db import models


class AlumnosYCursos(models.Model):
    Curso = models.ForeignKey(
        "Cursos.Curso", on_delete=models.CASCADE, blank=True, null=True
    )
    Alumno = models.ForeignKey(
        "Cursos.Alumno", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.Curso}, {self.Alumno}"


# Create your models here.
