from django.views import generic
from .models import Proyecto, Tarea
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, TareaForm, ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect



# Vista principal
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'cmmi/iniciar_sesion.html')
    else:
        proyectos = Proyecto.objects.filter(usuario=request.user)
        num_tareas_completas = [Tarea.objects.filter(proyecto=p, completada=True).count() for p in proyectos]
        num_tareas_total = [Tarea.objects.filter(proyecto=p).count() for p in proyectos]
        perc_compl = list()
        for comp, total in zip(num_tareas_completas, num_tareas_total):

            if total != 0:
                vall = float(comp/total)
                vall2 = float(vall)*float(100.0)
                perc_compl.append(round(float(vall2),1))
            else:
                perc_compl.append(0.0)
        proyectos_and_perc = zip(proyectos,perc_compl)

        return render(request, 'cmmi/index.html', {'proyectos': proyectos, 'proyectos_and_perc':proyectos_and_perc})


#Search
def search(request):
    resultado_tareas = Tarea.objects.all()
    query = request.GET.get("q")
    if query:
        proyectos = Proyecto.objects.filter(
            Q(nombre_proyecto__icontains=query) |
            Q(manager__icontains=query)
        ).distinct()
        resultado_tareas = resultado_tareas.filter(
            Q(nombre_tarea__icontains=query)
        ).distinct()
        # print(proyectos)
        num_tareas_completas = [Tarea.objects.filter(proyecto=p, completada=True).count() for p in proyectos]
        num_tareas_total = [Tarea.objects.filter(proyecto=p).count() for p in proyectos]
        perc_compl = list()
        for comp, total in zip(num_tareas_completas, num_tareas_total):
            if total != 0:
                vall = float(comp/total)
                vall2 = float(vall)*float(100.0)
                perc_compl.append(round(float(vall2),1))
            else:
                perc_compl.append(0.0)
        print(proyectos)
        proyectos_and_perc = zip(proyectos,perc_compl)
        return render(request, 'cmmi/index.html', {
            'proyectos_and_perc': proyectos_and_perc,
            'tareas': resultado_tareas,
            'proyectos':proyectos
        })
# Detalles
class VistaDetalles(generic.DetailView):
    login_url = '/iniciar_sesion/'
    redirect_field_name = 'redirect_to'
    model = Proyecto
    template_name = 'cmmi/detalles.html'

# Añadir nuevo proyecto
def proyecto_crear(request):
    if not request.user.is_authenticated():
        return render(request, 'cmmi/iniciar_sesion.html')
    else:
        form = ProyectoForm(request.POST or None)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return render(request, 'cmmi/detalles.html', {'proyecto': proyecto})
        context = {
            "form": form,
        }
        return render(request, 'cmmi/proyecto_crear.html', context)

# Modificar proyecto
def proyecto_modificar(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    form = ProyectoForm(request.POST or None, instance = proyecto)
    if form.is_valid():
        proyecto = form.save(commit=False)
        proyecto.save()
        return HttpResponseRedirect(proyecto.get_absolute_url())
    context = {
        "proyecto":proyecto,
        "form":form,
    }
    return render(request, 'cmmi/proyecto_form.html', context)


# Eliminar proyecto
class EliminaProyecto(DeleteView):
    login_url = '/iniciar_sesion/'
    redirect_field_name = 'redirect_to'
    model = Proyecto
    success_url = reverse_lazy('cmmi:index')


# Proyecto urgente
def proyecto_urgente(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    try:
        if proyecto.es_urgente:
            proyecto.es_urgente = False

        else:
            proyecto.es_urgente = True
        proyecto.save()
    except (KeyError, Proyecto.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

# Añadir nueva tarea
def tarea_crear(request, proyecto_id):
	form = TareaForm(request.POST or None)
	proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
	if form.is_valid():
		proyectos_tareas = proyecto.tarea_set.all()
		for t in proyectos_tareas:
			if t.nombre_tarea == form.cleaned_data.get("nombre_tarea"):
				context = {
					'proyecto': proyecto,
					'form': form,
					'error_message': 'Esta tarea ya ha sido añadida',
				}
				return render(request, 'cmmi/tarea_crear.html', context)
		tarea = form.save(commit=False)
		tarea.proyecto = proyecto
		tarea.completada = False
		tarea.save()
		return render(request, 'cmmi/detalles.html', {'proyecto': proyecto})
	context = {
		'proyecto': proyecto,
		'form': form,
	}
	return render(request, 'cmmi/tarea_crear.html', context)


# Eliminar tarea
def tarea_eliminar(request, proyecto_id, tarea_id):
	proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
	tarea = Tarea.objects.get(pk=tarea_id)
	tarea.delete()
	return render(request, 'cmmi/detalles.html', {'proyecto': proyecto})

# Ver tareas
def tareas(request, filter_by):
	if not request.user.is_authenticated():
		return render(request, 'cmmi/iniciar_sesion.html')
	else:
		try:
			tarea_ids = []
			for proyecto in Proyecto.objects.filter(usuario=request.user):
				for tarea in proyecto.tarea_set.all():
					tarea_ids.append(tarea.pk)
			tareas_usuario = Tarea.objects.filter(pk__in=tarea_ids)
			if filter_by == 'urgentes':
				tareas_usuario = tareas_usuario.filter(es_urgente=True)
		except Proyecto.DoesNotExist:
			tareas_usuario = []
		return render(request, 'cmmi/tareas.html', {
			'tareas': tareas_usuario,
			'filter_by': filter_by,
		})


# Tarea urgente
def urgente(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    try:
        if tarea.es_urgente:
            tarea.es_urgente = False
        else:
            tarea.es_urgente = True
        tarea.save()
    except (KeyError, Tarea.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

# Tarea completada
def completada(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if tarea.completada:
        tarea.completada = False
    else:
        tarea.completada = True
    tarea.save()
    return HttpResponseRedirect('/cmmi/%s' %tarea.proyecto.id)


def completadasAll(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    if tarea.completada:
        tarea.completada = False
    else:
        tarea.completada = True
    tarea.save()
    return HttpResponseRedirect('/cmmi/tareas/all')

#Registrar un usuario nuevo
def registro(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                proyectos = Proyecto.objects.filter(usuario=request.user)
                return render(request, 'cmmi/index.html', {'proyectos': proyectos})
    context = {
        "form": form,
    }
    return render(request, 'cmmi/registro.html', context)


# Iniciar sesión
def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                proyectos = Proyecto.objects.filter(usuario=request.user)
                return render(request, 'cmmi/index.html', {'proyectos': proyectos})
            else:
                return render(request, 'cmmi/iniciar_sesion.html', {'error_message': 'Se ha desactivado su cuenta.'})
        else:
            return render(request, 'cmmi/iniciar_sesion.html', {'error_message': 'Inicio de sesión inválido.'})
    return render(request, 'cmmi/iniciar_sesion.html')

# Cerrar sesión
class CerrarSesionView(View):
    def get(self, request):
        logout(request)
        form = UserForm(request.POST or None)
        context = {"form": form,}
        return render(request, 'cmmi/iniciar_sesion.html', context)
