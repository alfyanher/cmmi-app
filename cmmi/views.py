from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404

import json

def index(request):
    return HttpResponse("Hello, world. You're at the cmmi index.")

def createProject(request):
	if request.POST:
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save()
			project.save()
		else:
			print(form.errors)
	else:
		form = ProjectForm()
	return render(request, 'cmmi/project.html', locals())
#
# def modifyProject(request):
#     project = Proyecto.objects.get(id=request.GET.get('project_id',False))
#     form = ProjectForm(request.POST or None, instance = project)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)
#     return render(request, 'cmmi/project.html', locals())

def modifyProject(request):
    project = Proyecto.objects.get(id=request.GET.get('project_id',False))
    if request.POST:
        form = ProjectForm(request.POST)
        print(TODO)
    return render(request, 'cmmi/modifyProject.html',{'project' : project_id})

@csrf_exempt
def createTask(request):
    #print(request.GET.get('project_id'))
    print(request.method)
    project = Proyecto.objects.get(id=request.GET.get('project_id',False))
    print(project.id)

    if request.POST:
        print("ESTOY DENTROOOOO")
        form = TaskForm(request.POST)
        print("ESTOY DENTROOOOO 2")
        if form.is_valid():
            task = form.save()
            task.save()
            print("ESTOY DENTROOOOO 3")
        else:
            print(form.errors)
    else:
        form = TaskForm()
        print(TaskForm)
    return render(request, 'cmmi/task.html',{'project' : project})

#
#     print(request.GET.get('project_id',False))
#     project = Proyecto.objects.get(id=request.GET.get('project_id',False))
#     # tasks = Tarea.objects.filter(proyecto_id=project.id)
#     # if request.POST:
#     #     form = TaskForm(request.POST)
#     #     form.proyecto_id = int(request.GET.get('project_id'))
#     #     form.proyecto = project
#     #     if form.is_valid():
#     #         task = form.save()
#     #         return HttpResponseRedirect('/projectDetails')
#     #     else:
#     #         print(form.errors)
#     # else:
#     #     form = TaskForm()
#     return render(request, 'cmmi/task.html', locals())
# #
# def modifyTask(request):
#     task = Tarea.objects.get(id=request.GET.get('task_id',False))
#     form = TaskForm(request.POST or None, instance = task)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)
#     return render(request, 'cmmi/modifyTask.html', locals())


def listAllProjects(request):
    projects = Proyecto.objects.all()
    return render(request, 'cmmi/listAllProjects.html', locals())

# def listTasksPerProject(request):
#     tasks = Tarea.objects.filter(id=request.GET['project'])
#     return render(request, 'cmmi/listTasksPerProject.html', locals())

def projectDetails(request):
    print(request.GET.get('project_id'))
    print('Ha pasado!!!!')
    project = Proyecto.objects.get(id=request.GET.get('project_id',False))
    tasks = Tarea.objects.filter(proyecto_id=project.id)
    return render(request, 'cmmi/projectDetails.html', locals())

def taskDetails(request):
    task = Tarea.objects.get(id=request.GET['task_id'])
    return render(request, 'cmmi/taskDetails.html', locals())
