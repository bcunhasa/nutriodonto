# Generated by Django 2.1.3 on 2018-11-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0009_auto_20181112_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='nome',
        ),
        migrations.AddField(
            model_name='aluno',
            name='numero_identificacao',
            field=models.CharField(default=0, max_length=200, verbose_name='Número de identificação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='raça',
            field=models.CharField(choices=[('0', 'Amarela'), ('1', 'Branca'), ('2', 'Indígena'), ('3', 'Parda'), ('4', 'Preta')], default=1, max_length=2, verbose_name='Raça'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionario',
            name='data',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('0', 'Masculino'), ('1', 'Feminino'), ('2', 'Outro'), ('3', 'Prefiro não responder')], max_length=2, verbose_name='Sexo'),
        ),
    ]
