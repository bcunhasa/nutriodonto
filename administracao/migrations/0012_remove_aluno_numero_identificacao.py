# Generated by Django 2.1.3 on 2018-11-12 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0011_auto_20181112_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='numero_identificacao',
        ),
    ]
