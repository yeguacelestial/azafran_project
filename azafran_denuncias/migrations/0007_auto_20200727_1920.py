# Generated by Django 3.0.6 on 2020-07-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('azafran_denuncias', '0006_auto_20200727_1755'),
        ('azafran_denuncias', '0005_denunciapublicada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denunciapublicada',
            name='genero',
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='edad',
            field=models.CharField(choices=[('', 'Selecciona un rango de edad'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 11 a 15 años', 'De 11 a 15 años'), ('De 16 a 20 años', 'De 16 a 20 años'), ('De 21 a 25 años', 'De 21 a 25 años'), ('De 26 a 30 años', 'De 26 a 30 años'), ('De 26 a 30 años', 'De 26 a 30 años'), ('Más de 30 años', 'Más de 30 años')], max_length=30),
        ),
    ]
