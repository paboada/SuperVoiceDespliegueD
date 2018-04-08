# Generated by Django 2.0.2 on 2018-02-25 16:50

import WebConcursos.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebConcursos', '0009_auto_20180224_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioLocutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('observaciones', models.CharField(max_length=1000)),
                ('descripcion_audio', models.CharField(max_length=100, null=True)),
                ('archivo_original', models.FileField(default='Null', upload_to='', validators=[WebConcursos.validators.validar_formato])),
                ('archivo_convertido', models.FileField(default='Null', upload_to='convert')),
                ('estado', models.CharField(default='En Proceso', max_length=100)),
                ('seleccionado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_concurso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='concurso', to='WebConcursos.Concurso')),
            ],
        ),
    ]
