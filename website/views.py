from django.shortcuts import redirect, render
from website.forms import FormularioForm, NoticiasForm, EventosForm
from website.models import Formulario, Noticias, Eventos

# -----------------PÁGINA PRINCIPAL---------------------------
# -----------------VISTA DESDE USUARIOS-----------------------

def home(request):
    return render(request, 'usuarios/home.html')


def informacion(request):
    return render(request, 'usuarios/informacion.html')


# ---------------------TIPOS DE CÁNCER---------------------------
def cancerColon(request):
    return render(request, 'usuarios/tiposCancer/colon.html')


def cancerCuelloUtero(request):
    return render(request, 'usuarios/tiposCancer/cuelloUtero.html')


def cancerMama(request):
    return render(request, 'usuarios/tiposCancer/mama.html')


def cancerPiel(request):
    return render(request, 'usuarios/tiposCancer/piel.html')


def cancerProstata(request):
    return render(request, 'usuarios/tiposCancer/prostata.html')


def cancerPulmon(request):
    return render(request, 'usuarios/tiposCancer/pulmon.html')


# -----------SOLICITUDES DE SOCIO----------------


def formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('website:formulario')
    else:
        form = FormularioForm()
    return render(request, 'usuarios/formulario.html', {'form': form})


# ----------MOSTRAR NOTICIAS Y EVENTOS-----------
def noticias(request):
    noticia = Noticias.objects.all().order_by('-id_noticia')
    context = {'noticias': noticia}
    return render(request, 'usuarios/noticias.html', context)


def eventos(request):
    evento = Eventos.objects.all().order_by('-id_evento')
    context = {'eventos': evento}
    return render(request, 'usuarios/eventos.html', context)
