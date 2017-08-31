from django.contrib.auth.models import User
from django import forms

from .models import Proyecto, Tarea

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto', 'descripcion', 'fecha_inicio', 'manager', 'nivelMadurez']

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['nombre_tarea', 'descripcion', 'categoriaAP']
