from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

    def Mostrar_Cantidad_Cursos(self):
        alumno = Alumno.objects.get(id=self.id)
        cursos = Curso.objects.filter(alumnos=alumno)
        return len(cursos)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    diasDeLaSemana = models.CharField(max_length=100)
    fechaDeInicio = models.DateField()
    fechaDeFinalizacion = models.DateField()
    instructor = models.ForeignKey(
        "Instructor", on_delete=models.CASCADE, blank=True, null=True
    )
    alumnos = models.ManyToManyField(Alumno, through="AlumnoCursos")

    def __str__(self):
        return self.nombre

    def Mostrar_Cantidad_Alumnos(self):
        return self.alumnos.count()


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


class AlumnoCursos(models.Model):
    Alumno = models.ForeignKey(
        "Alumno", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    Curso = models.ForeignKey(
        "Curso", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    estadoInscripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Alumno}, {self.Curso}, - {self.estadoInscripcion}"


# Create your models here.
