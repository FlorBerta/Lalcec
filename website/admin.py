from django.contrib import admin
from website.models import Formulario, Noticias, Eventos
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

admin.site.register(Formulario)
admin.site.register(Noticias)
admin.site.register(Eventos)