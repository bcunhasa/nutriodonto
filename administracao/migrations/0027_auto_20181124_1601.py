# Generated by Django 2.1.3 on 2018-11-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0026_auto_20181124_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretor',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data de preenchimento'),
        ),
    ]