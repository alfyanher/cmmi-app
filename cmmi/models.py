from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

@python_2_unicode_compatible
class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    fecha_inicio = models.DateTimeField('fecha de inicio')
    fecha_final_estimada = models.DateTimeField('fecha estimada de finalizacion', blank=True, null=True,)
    porcentaje_completado = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.nombre_proyecto

    def __unicode__(self):
        return self.nombre_proyecto

@python_2_unicode_compatible
class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 400)
    comentarios = models.CharField(max_length = 400)
    proyecto_id = models.ForeignKey('Proyecto', db_column='proyecto_id', models.SET_NULL, null=True, blank=True)
    porcentaje_completado = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])


    def __str__(self):
        return self.nombre_tarea

    def __unicode__(self):
        return self.nombre_tarea
