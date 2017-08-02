"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cmmi import views



urlpatterns = [
    url(r'^cmmi/', include('cmmi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^project/', views.createProject, name='createProject'),
    url(r'^task/', views.createTask, name='createTask'),
    url(r'^modifyProject/', views.modifyProject, name='modifyProject'),
    # url(r'^modifyTask/', views.modifyTask, name='modifyTask'),
    url(r'^listAllProjects/', views.listAllProjects, name='listAllProjects'),
    #url(r'^listTasksPerProject/', views.listTasksPerProject, name='listTasksPerProject'),
    url(r'^projectDetails/', views.projectDetails, name='projectDetails'),
    url(r'^taskDetails/', views.taskDetails, name='taskDetails'),
    ]
