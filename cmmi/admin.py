from django.contrib import admin

from .models import Proyecto
from .models import Tarea

admin.site.register(Proyecto)
admin.site.register(Tarea)
