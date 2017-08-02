from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tarea
        #fields = ('nombre_tarea', 'descripcion', 'comentarios', 'porcentaje_completado')
        fields = '__all__'
