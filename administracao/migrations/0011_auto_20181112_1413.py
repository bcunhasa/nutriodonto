# Generated by Django 2.1.3 on 2018-11-12 17:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0010_auto_20181112_0924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diretor',
            options={'verbose_name': 'Questionário para diretores', 'verbose_name_plural': 'Questionários para diretores'},
        ),
        migrations.AlterField(
            model_name='escola',
            name='nome',
            field=models.CharField(choices=[('Escola municipal Antônio Carlos Jobim', 'Escola municipal Antônio Carlos Jobim'), ('Escola municipal Antônio G. de Carvalho Filho', 'Escola municipal Antônio G. de Carvalho Filho'), ('Escola municipal Anne Frank', 'Escola municipal Anne Frank'), ('Escola municipal Darcy Ribeiro', 'Escola municipal Darcy Ribeiro'), ('Escola municipal Henrique Talone Pinheiro', 'Escola municipal Henrique Talone Pinheiro'), ('Escola municipal de T.I. Vinícius de Moraes', 'Escola municipal de T.I. Vinícius de Moraes'), ('Escola municipal Beatriz Rodrigues da Silva', 'Escola municipal Beatriz Rodrigues da Silva'), ('Escola municipal Mestre Pacífico S. Campos', 'Escola municipal Mestre Pacífico S. Campos'), ('Escola municipal Luiz Gonzaga', 'Escola municipal Luiz Gonzaga'), ('Escola municipal de T.I. Padre Josimo M. Tavares', 'Escola municipal de T.I. Padre Josimo M. Tavares'), ('Escola municipal de T.I. Daniel Batista', 'Escola municipal de T.I. Daniel Batista'), ('Escola municipal de T.I. Monsenhor Pedro P. Piagem', 'Escola municipal de T.I. Monsenhor Pedro P. Piagem'), ('Escola municipal Jorge Amado', 'Escola municipal Jorge Amado'), ('Escola municipal Maria Rosa de Castro Sales', 'Escola municipal Maria Rosa de Castro Sales'), ('Escola municipal Professor Sávia F. Jacome', 'Escola municipal Professor Sávia F. Jacome'), ('Escola municipal de T.I. Caroline C. C. da Silva', 'Escola municipal de T.I. Caroline C. C. da Silva'), ('Escola municipal Aurélio Buarque de Holanda', 'Escola municipal Aurélio Buarque de Holanda'), ('Escola municipal Maria Júlia Amorim Rodrigues', 'Escola municipal Maria Júlia Amorim Rodrigues'), ('Escola municipal Thiago Barbosa', 'Escola municipal Thiago Barbosa'), ('Escola municipal de T.I. Euridice F. de Mello', 'Escola municipal de T.I. Euridice F. de Mello'), ('Escola municipal de T.I. Margarida Gonçalves', 'Escola municipal de T.I. Margarida Gonçalves'), ('Escola municipal Crispim Pereira de Alencar', 'Escola municipal Crispim Pereira de Alencar'), ('Escola municipal de T.I. Aprigio T. de Matos', 'Escola municipal de T.I. Aprigio T. de Matos'), ('Escola municipal de T.I. João Beltrão', 'Escola municipal de T.I. João Beltrão'), ('Escola municipal de T.I. Luiz Nunes de Oliveira', 'Escola municipal de T.I. Luiz Nunes de Oliveira'), ('Escola municipal de T.I. Sueli Pereira A. Reche', 'Escola municipal de T.I. Sueli Pereira A. Reche'), ('Escola Silverio Ribeiro Matos', 'Escola Silverio Ribeiro Matos (Mumbuca)'), ('Escola de teste', 'Escola de teste')], max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='questao_129',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='129. Alguma vez na vida você foi forçado(a) a ter relação sexual?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='questao_146',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('0', 'Fácil'), ('1', 'Difícil'), ('2', 'Chato'), ('3', 'Legal'), ('4', 'Interessante'), ('5', 'Informativo'), ('6', 'Cansativo'), ('7', 'Constrangedor')], max_length=2), blank=True, null=True, size=None, verbose_name='146. O que você achou deste questionário?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='questao_60',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('0', 'Leite + papinhas'), ('1', 'Leite + sopas'), ('2', 'Leite + frutas')], max_length=2), blank=True, null=True, size=None, verbose_name='60. Até dois anos de idade, seu filho ou sua filha recebeu alimentação mista, isto é:'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='questao_7',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='07. Você tem celular?'),
        ),
    ]