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
]

