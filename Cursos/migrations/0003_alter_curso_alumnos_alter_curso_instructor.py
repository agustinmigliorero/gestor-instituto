# Generated by Django 4.2.6 on 2023-11-01 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0002_alter_curso_alumnos_alter_curso_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(blank=True, null=True, to='Cursos.alumno'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.instructor'),
        ),
    ]
