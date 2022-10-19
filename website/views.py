from django.shortcuts import redirect, render
from website.forms import FormularioForm, NoticiasForm, EventosForm
from website.models import Formulario, Noticias, Eventos
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


# ------------------------INICIAR SESIÓN--------------------------------
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada: {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido registrado como {nombre_usuario}")
            return redirect("website:Home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = UserCreationForm
    return render(request, 'login/register.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {usuario}")
                return redirect('website:homeAdministrador')
            else:
                messages.error(request, "Usuario o contraseña equivocada")
        else:
            messages.error(request, "Usario o contraseña equivocada")
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("website:home")


# ------------------------ADMINISTRADOR DE LALCEC----------------------------------
@login_required(login_url='login/login.html')
def homeAdmin(request):
    return render(request, 'administrador/homeAdmin.html')


# -------------------------SOLICITUDES-----------------------------------------
@login_required(login_url='login/login.html')
def solicitudesAdmin(request):
    solicitud = Formulario.objects.all().order_by('-id_formulario')
    context = {'solicitudes': solicitud}
    return render(request, 'administrador/solicitudesAdmin.html', context)


@login_required(login_url='login/login.html')
def solicitudes_delete(request, id_formulario):
    solicitud = Formulario.objects.get(id_formulario=id_formulario)

    if request.method == 'POST':
        solicitud.delete()
        return redirect('website:solicitudesAdmin')
    return render(request, 'administrador/solicitudesDelete.html', {'solicitud': solicitud})


# --------------------------EVENTOS---------------------------------
@login_required(login_url='login/login.html')
def eventosAdmin(request):
    evento = Eventos.objects.all().order_by('-id_evento')
    context = {'eventos': evento}
    return render(request, 'administrador/eventosAdmin.html', context)


@login_required(login_url='login/login.html')
def nuevoEvento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('website:nuevoEvento')
    else:
        form = EventosForm()

    return render(request, 'administrador/nuevoEvento.html', {'form': form})


@login_required(login_url='login/login.html')
def eventos_delete(request, id_evento):
    evento = Eventos.objects.get(id_evento=id_evento)
    if request.method == 'POST':
        evento.delete()
        return redirect('website:eventosAdmin')
    return render(request, 'administrador/eventosDelete.html', {'evento': evento})


@login_required(login_url='login/login.html')
def modificarEvento(request, id_evento):
    evento = Eventos.objects.get(id_evento=id_evento)
    if request.method == 'GET':
        form = EventosForm(instance=evento)
    else:
        form = EventosForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
        return redirect('website:eventosAdmin')
    return render(request, 'administrador/modificarEvento.html', {'form': form})


# ---------------------------NOTICIAS---------------------------------
@login_required(login_url='login/login.html')
def noticiasAdmin(request):
    noticia = Noticias.objects.all().order_by('-id_noticia')
    context = {'noticias': noticia}
    return render(request, 'administrador/noticiasAdmin.html', context)


@login_required(login_url='login/login.html')
def nuevaNoticia(request):
    if request.method == 'POST':
        form = NoticiasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('website:nuevaNoticia')
    else:
        form = NoticiasForm()
    return render(request, 'administrador/nuevaNoticia.html', {'form': form})


@login_required(login_url='login/login.html')
def noticias_delete(request, id_noticia):
    noticia = Noticias.objects.get(id_noticia=id_noticia)

    if request.method == 'POST':
        noticia.delete()
        return redirect('website:noticiasAdmin')
    return render(request, 'administrador/noticiasDelete.html', {'noticia': noticia})


@login_required(login_url='login/login.html')
def modificarNoticia(request, id_noticia):
    noticia = Noticias.objects.get(id_noticia=id_noticia)
    if request.method == 'GET':
        form = NoticiasForm(instance=noticia)
    else:
        form = NoticiasForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
        return redirect('website:noticiasAdmin')
    return render(request, 'administrador/modificarNoticia.html', {'form': form})