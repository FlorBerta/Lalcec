# Generated by Django 4.1.1 on 2022-10-05 22:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='desarrollo_evento',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='desarrollo_noticia',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
