# Generated by Django 2.2.3 on 2019-09-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('url', models.CharField(max_length=200, verbose_name='URL do documento')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('url', models.CharField(max_length=200, verbose_name='URL da foto')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data', models.CharField(max_length=200, verbose_name='Data de criação')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('imagem', models.CharField(max_length=200, verbose_name='URL da imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('url', models.CharField(max_length=200, verbose_name='URL do vídeo')),
            ],
        ),
    ]
