# Generated by Django 4.1.1 on 2022-10-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id_evento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_evento', models.DateField(auto_now_add=True)),
                ('titulo_evento', models.CharField(max_length=100)),
                ('desarrollo_evento', models.TextField(max_length=1000)),
                ('imagen_evento', models.ImageField(null=True, upload_to='media/evento')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id_noticia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_noticia', models.DateField(auto_now_add=True)),
                ('titulo_noticia', models.CharField(max_length=100)),
                ('desarrollo_noticia', models.TextField(max_length=1000)),
                ('imagen_noticia', models.ImageField(null=True, upload_to='media/noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id_formulario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('domicilio', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('pago', models.ManyToManyField(blank=True, to='website.pago')),
            ],
        ),
    ]
