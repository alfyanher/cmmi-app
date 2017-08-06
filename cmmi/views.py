from django.views import generic
from .models import Proyecto, Tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class VistaPrincipal(generic.ListView):
    template_name = 'cmmi/index.html'
    context_object_name = 'lista_proyecto'

    def get_queryset(self):
        return Proyecto.objects.all()

class VistaDetalles(generic.DetailView):
    model = Proyecto
    template_name = 'cmmi/detalles.html'

class CreaProyecto(CreateView):
    model = Proyecto
    fields = ['nombre_proyecto', 'descripcion', 'fecha_inicio', 'manager']

class ModificaProyecto(UpdateView):
    model = Proyecto
    fields = ['nombre_proyecto', 'descripcion', 'fecha_inicio', 'manager']

class EliminaProyecto(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('cmmi:index')

class VistaUsuarioForm(View):
    form_class = UserForm
    template_name = 'cmmi/registro.html'

    # Formulario en blanco
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #Procesa la info
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)

            #datos formateados
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()

            #devuelve al Usuario si los credenciales son correctos
            usario = authenticate(username=username,password=password)

            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return redirect('cmmi:index')
                    
        return render(request, self.template_name, {'form': form})
