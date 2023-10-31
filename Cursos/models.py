from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Create your models here.
