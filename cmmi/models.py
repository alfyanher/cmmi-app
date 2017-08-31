from django.db import models
from datetime import datetime
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    fecha_inicio = models.DateField(default=datetime.now, blank=True)
    manager = models.CharField(max_length=100)
    es_urgente = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, default=1)
    NIVEL = (
        ('Ejecutado','Ejecutado'),
        ('Gestionado','Gestionado'),
        ('Definido','Definido'),
        ('Gestionado Cuantitativamente','Gestionado Cuantitativamente'),
        ('Optimizado','Optimizado'),
        )
    nivelMadurez = models.CharField(max_length=100, default='Incompleto', choices=NIVEL, verbose_name = 'Nivel de madurez')

    def get_absolute_url(self):
        return reverse('cmmi:detalles', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.nombre_proyecto + " - " +  self.manager

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 400)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    es_urgente = models.BooleanField(default=False)
    completada = models.BooleanField(default=False)
    CATEGORIA = (
        ('Gestión de proyecto','Gestión de proyecto'),
        ('Gestión de procesos','Gestión de procesos'),
        ('Ingeniería','Ingeniería'),
        ('Soporte','Soporte'),
        )
    categoriaAP = models.CharField(max_length=100, default = '--', choices=CATEGORIA, verbose_name = 'Categoría')

    def __str__(self):
        return self.nombre_tarea
