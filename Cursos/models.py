from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    diasDeLaSemana = models.CharField(max_length=100)
    fechaDeInicio = models.DateField()
    fechaDeFinalizacion = models.DateField()
    instructor = models.ForeignKey(
        "Instructor", on_delete=models.CASCADE, blank=True, null=True
    )
    alumnos = models.ManyToManyField("Alumno", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    # cursos = models.ManyToManyField("Curso")

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    # cursos = models.ManyToManyField("Curso")

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


# Create your models here.
