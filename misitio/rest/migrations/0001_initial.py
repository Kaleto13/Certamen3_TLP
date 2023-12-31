# Generated by Django 4.2.6 on 2023-11-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('1', 'Vacaciones'), ('2', 'Feriado'), ('3', 'Suspensión de actividades'), ('4', 'Suspensión de actividades PM'), ('5', 'Período Lectivo'), ('6', 'Suspensión de evaluaciones'), ('7', 'Ceremonia'), ('8', 'EDDA'), ('9', 'Evaluación'), ('10', 'Ayudantías'), ('11', 'Hito Académico'), ('12', 'Secretaría Académica'), ('13', 'OAI')], default='Vacaciones', max_length=2)),
                ('segmento', models.CharField(choices=[('C', 'Comunidad USM'), ('E', 'Estudiante'), ('P', 'Profesor'), ('J', 'Jefe de Carrera')], default='Comunidad USM', max_length=1)),
            ],
        ),
    ]
