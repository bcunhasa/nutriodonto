# Generated by Django 2.1 on 2018-08-30 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='campanha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acoes', to='administracao.Campanha'),
        ),
    ]
