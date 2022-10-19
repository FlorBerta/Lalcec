from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


#Checkbox método de pago
class Pago(models.Model):
    metodo = models.CharField(max_length=10)

    def __str__(self):
        return'{}'.format(self.metodo)

#Formulario para solicitar ser socio/a
class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.IntegerField()
    pago = models.ManyToManyField(Pago, blank=True)

    class Meta():
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'

    def __str__(self):
        return self.id_formulario

#Subir nueva noticia
class Noticias(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    fecha_noticia = models.DateField(auto_now_add=True, blank=True)
    titulo_noticia = models.CharField(max_length=100)
    desarrollo_noticia = RichTextField()
    imagen_noticia = models.ImageField(upload_to='media/noticia', null=True)

    class Meta():
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo_noticia

#Subir  nuevo evento
class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    fecha_evento = models.DateField(auto_now_add=True, blank=True)
    titulo_evento = models.CharField(max_length=100)
    desarrollo_evento = RichTextField()
    imagen_evento = models.ImageField(upload_to='media/evento', null=True)

    class Meta():
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo_evento