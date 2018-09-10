# Generated by Django 2.1 on 2018-08-31 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0004_auto_20180831_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='nome',
            field=models.CharField(choices=[('Escola municipal Antônio Carlos Jobim', 'Escola municipal Antônio Carlos Jobim'), ('Escola municipal Antônio G. de Carvalho Filho', 'Escola municipal Antônio G. de Carvalho Filho'), ('Escola municipal Anne Frank', 'Escola municipal Anne Frank'), ('Escola municipal Darcy Ribeiro', 'Escola municipal Darcy Ribeiro'), ('Escola municipal Henrique Talone Pinheiro', 'Escola municipal Henrique Talone Pinheiro'), ('Escola municipal de T.I. Vinícius de Moraes', 'Escola municipal de T.I. Vinícius de Moraes'), ('Escola municipal Beatriz Rodrigues da Silva', 'Escola municipal Beatriz Rodrigues da Silva'), ('Escola municipal Mestre Pacífico S. Campos', 'Escola municipal Mestre Pacífico S. Campos'), ('Escola municipal Luiz Gonzaga', 'Escola municipal Luiz Gonzaga'), ('Escola municipal de T.I. Padre Josimo M. Tavares', 'Escola municipal de T.I. Padre Josimo M. Tavares'), ('Escola municipal de T.I. Daniel Batista', 'Escola municipal de T.I. Daniel Batista'), ('Escola municipal de T.I. Monsenhor Pedro P. Piagem', 'Escola municipal de T.I. Monsenhor Pedro P. Piagem'), ('Escola municipal Jorge Amado', 'Escola municipal Jorge Amado'), ('Escola municipal Maria Rosa de Castro Sales', 'Escola municipal Maria Rosa de Castro Sales'), ('Escola municipal Professor Sávia F. Jacome', 'Escola municipal Professor Sávia F. Jacome'), ('Escola municipal de T.I. Caroline C. C. da Silva', 'Escola municipal de T.I. Caroline C. C. da Silva'), ('Escola municipal Aurélio Buarque de Holanda', 'Escola municipal Aurélio Buarque de Holanda'), ('Escola municipal Maria Júlia Amorim Rodrigues', 'Escola municipal Maria Júlia Amorim Rodrigues'), ('Escola municipal Thiago Barbosa', 'Escola municipal Thiago Barbosa'), ('Escola municipal de T.I. Euridice F. de Mello', 'Escola municipal de T.I. Euridice F. de Mello'), ('Escola municipal de T.I. Margarida Gonçalves', 'Escola municipal de T.I. Margarida Gonçalves'), ('Escola municipal Crispim Pereira de Alencar', 'Escola municipal Crispim Pereira de Alencar'), ('Escola municipal de T.I. Aprigio T. de Matos', 'Escola municipal de T.I. Aprigio T. de Matos'), ('Escola municipal de T.I. João Beltrão', 'Escola municipal de T.I. João Beltrão'), ('Escola municipal de T.I. Luiz Nunes de Oliveira', 'Escola municipal de T.I. Luiz Nunes de Oliveira'), ('Escola municipal de T.I. Sueli Pereira A. Reche', 'Escola municipal de T.I. Sueli Pereira A. Reche')], max_length=200, verbose_name='Nome'),
        ),
    ]