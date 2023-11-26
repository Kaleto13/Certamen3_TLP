from django.db import models


class Evento(models.Model):

    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    tipos = [('Vacaciones'),('Feriado'),('Suspensión de actividades'),('Suspensión de actividades PM'),('Período Lectivo'),('Suspensión de evaluaciones'),('Ceremonia'),('EDDA'),('Evaluación'),('Ayudantías'),('Hito Académico'),('Secretaría Académica'),('OAI')]  
    tipo = models.CharField(max_length=1,choices=tipos,default='Vacaciones')
    segmentos = [('Comunidad USM'),('Estudiante'),('Profesor'),('Jefe de Carrera')]
    segmento = models.CharField(choices=segmentos,default='Comunidad USM')


# Create your models here.
