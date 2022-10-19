from django.urls import path
from .views import formulario
from . import views

app_name = "website"

urlpatterns = [
    # pagina principal-usuario
    path('', views.home, name="Home"),
    path('informacion', views.informacion, name="Informacion"),

    path('tiposCancer/colon', views.cancerColon, name="Cancer de Colon"),
    path('tiposCancer/cuelloUtero', views.cancerCuelloUtero, name="Cancer de Cuello de Utero"),
    path('tiposCancer/mama', views.cancerMama, name="Cancer de Mama"),
    path('tiposCancer/piel', views.cancerPiel, name="Cancer de Piel"),
    path('tiposCancer/prostata', views.cancerProstata, name="Cancer de Prostata"),
    path('tiposCancer/pulmon', views.cancerPulmon, name="Cancer de Pulmon"),

    path('formulario', formulario, name="formulario"),
    path('noticias', views.noticias, name="noticias"),
    path('eventos', views.eventos, name="eventos"),

    # cuentas registar e iniciar sesión
    path('registro', views.registro, name="registro"),
    path('login', views.login_request, name="login"),
    path('logout', views.login_request, name="logout"),

    # administrador
    path('administrador/homeAdmin', views.homeAdmin, name="homeAdministrador"),

    path('administrador/solicitudesAdmin', views.solicitudesAdmin, name="solicitudesAdmin"),
    path('administrador/solicitudesDelete/<id_formulario>/', views.solicitudes_delete, name="solicitudesDelete"),

    path('administrador/eventosAdmin', views.eventosAdmin, name="eventosAdmin"),
    path('administrador/nuevoEvento', views.nuevoEvento, name="nuevoEvento"),
    path('administrador/eventosDelete/<id_evento>/', views.eventos_delete, name="eventosDelete"),
    path('modificarEvento/<id_evento>/', views.modificarEvento, name="modificarEvento"),

    path('administrador/noticiasAdmin', views.noticiasAdmin, name="noticiasAdmin"),
    path('administrador/nuevaNoticia', views.nuevaNoticia, name="nuevaNoticia"),
    path('administrador/noticiaDelete/<id_noticia>/', views.noticias_delete, name="noticiasDelete"),
    path('modificarNoticia/<id_noticia>/', views.modificarNoticia, name="modificarNoticia"),
]

