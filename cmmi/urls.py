from django.conf.urls import url
from . import views

app_name ='cmmi'

urlpatterns = [

    #Principal
    url(r'^$', views.VistaPrincipal.as_view(), name='index'),
    #Registro
    url(r'^registro/$', views.VistaUsuarioForm.as_view(), name='registro'),
    #Delalles
    url(r'^(?P<pk>[0-9]+)/$',views.VistaDetalles.as_view(), name='detalles'),
    #Crea
    url(r'proyecto/crear/$',views.CreaProyecto.as_view(), name='proyecto-crear'),
    #Modifica
    url(r'proyecto/(?P<pk>[0-9]+)/$',views.ModificaProyecto.as_view(), name='proyecto-modificar'),
    #Elimina
    url(r'proyecto/(?P<pk>[0-9]+)/eliminar/$',views.EliminaProyecto.as_view(), name='proyecto-eliminar'),

]
