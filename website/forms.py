from django import forms
from website.models import Formulario, Noticias, Eventos

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'id_formulario',
            'apellido',
            'nombre',
            'dni',
            'domicilio',
            'localidad',
            'telefono',
        ]
        labels = {
            'id_formulario' : 'Id_Formulario',
            'apellido' : 'Apellido',
            'nombre' : 'Nombre',
            'dni' : 'DNI',
            'domicilio' : 'Domicilio',
            'localidad' : 'Localidad',
            'telefono' : 'Telefono',
        }
        widgets = {
            'id_formulario' : forms.NumberInput(attrs={'class':'forms-control'}),
            'apellido' : forms.TextInput(attrs={'class':'forms-control'}),
            'nombre' : forms.TextInput(attrs={'class':'forms-control'}),
            'dni' : forms.NumberInput(attrs={'class':'forms-control'}),
            'domicilio' : forms.TextInput(attrs={'class':'forms-control'}),
            'localidad' : forms.TextInput(attrs={'class':'forms-control'}),
            'telefono' : forms.NumberInput(attrs={'class':'forms-control'}),
        }

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = [
            'id_noticia',
            'titulo_noticia',
            'desarrollo_noticia',
            'imagen_noticia',
        ]
        labels = {
            'id_noticia' : 'id Noticia',
            'titulo_noticia' : 'Titulo de la Noticia',
            'desarrollo_noticia' : 'Desarrollo de la Noticia',
            'imagen_noticia' : 'Imagen Noticia',

        }
        widgets = {
            'id_noticia' : forms.NumberInput(attrs={'class':'forms-control'}),
            'titlo_noticia' : forms.TextInput(attrs={'class':'forms-control'}),
            'desarrollo_noticia' : forms.Textarea(attrs={'class':'forms-control'}),
        }

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = [
            'id_evento',
            'titulo_evento',
            'desarrollo_evento',
            'imagen_evento',
        ]
        labels = {
            'id_evento' : 'id Evento',
            'titulo_evento' : 'Titulo Evento',
            'desarrollo_evento' : 'Desarrollo Evento',
            'imagen_evento' : 'Imagen Evento',

        }
        widgets = {
            'id_evento' : forms.NumberInput(attrs={'class':'forms-control'}),
            'titlo_evento' : forms.TextInput(attrs={'class':'forms-control'}),
            'desarrollo_evento' : forms.Textarea(attrs={'class':'forms-control'}),
        }
