from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/', views.createProject, name='createProject'),
    url(r'^task/', views.createTask, name='createTask'),
]
