from django.db import models


class Evento(models.Model):

    id = models.BigAutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    tipos = [('1','Vacaciones'),('2','Feriado'),('3','Suspensión de actividades'),('4','Suspensión de actividades PM'),('5','Período Lectivo'),('6','Suspensión de evaluaciones'),('7','Ceremonia'),('8','EDDA'),('9','Evaluación'),('10','Ayudantías'),('11','Hito Académico'),('12','Secretaría Académica'),('13','OAI')]  
    tipo = models.CharField(max_length=2,choices=tipos,default='Vacaciones')
    segmentos = [('C','Comunidad USM'),('E','Estudiante'),('P','Profesor'),('J','Jefe de Carrera')]
    segmento = models.CharField(max_length=1,choices=segmentos,default='Comunidad USM')

#class Evento(models.Model):
 #   fullname = models.CharField(max_length=100)
  #  nickname = models.CharField(max_length=50)
   # age = models.PositiveSmallIntegerField()
   # is_active = models.BooleanField(default=True)

# Create your models here.
