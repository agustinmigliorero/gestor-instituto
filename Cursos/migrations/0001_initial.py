# Generated by Django 4.2.6 on 2023-11-01 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField()),
                ('documento', models.IntegerField()),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField()),
                ('documento', models.IntegerField()),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('diasDeLaSemana', models.CharField(max_length=100)),
                ('fechaDeInicio', models.DateField()),
                ('fechaDeFinalizacion', models.DateField()),
                ('alumnos', models.ManyToManyField(to='Cursos.alumno')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.instructor')),
            ],
        ),
    ]
