from django.conf.urls import url
from . import views

app_name ='cmmi'

urlpatterns = [

    #Principal
    url(r'^$', views.index, name='index'),
    #Registro
    url(r'^registro/$', views.registro, name='registro'),

    #Sesión
    url(r'^iniciar_sesion/$', views.iniciar_sesion, name='iniciar_sesion'),
    url(r'^cerrar_sesion/$', views.CerrarSesionView.as_view(), name='cerrar_sesion'),

    #Detalles, Crear, Modificar y Eliminar un proyecto
    url(r'^(?P<pk>[0-9]+)/$',views.VistaDetalles.as_view(), name='detalles'),
    url(r'proyecto_crear/$',views.proyecto_crear, name='proyecto_crear'),
#    url(r'proyecto/(?P<pk>[0-9]+)/$',views.ModificaProyecto.as_view(), name='proyecto-modificar'),
    url(r'proyecto/(?P<pk>[0-9]+)/eliminar/$',views.EliminaProyecto.as_view(), name='proyecto-eliminar'),

    #Ver todas, Crear y Eliminar tareas
    url(r'^(?P<proyecto_id>[0-9]+)/tarea_crear/$', views.tarea_crear, name='tarea_crear'),
    url(r'^tareas/(?P<filter_by>[a-zA_Z]+)/$', views.tareas, name='tareas'),
    url(r'^(?P<proyecto_id>[0-9]+)/tarea_eliminar/(?P<tarea_id>[0-9]+)/$', views.tarea_eliminar, name='tarea_eliminar'),

    #Tarea y proyecto urgentes
    url(r'^(?P<tarea_id>[0-9]+)/urgente/$', views.urgente, name='urgente'),
    url(r'^(?P<proyecto_id>[0-9]+)/proyecto_urgente/$', views.proyecto_urgente, name='proyecto_urgente'),

    #url(r'^(?P<proyecto_id>[0-9]+)/proyecto_urgente/$', views.proyecto_urgente, name='proyecto_urgente'),

]
