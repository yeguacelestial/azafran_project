# Generated by Django 3.0.6 on 2020-07-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.CharField(choices=[('', 'Selecciona un rango de edad'), ('De 5 a 10 años', 'De 5 a 10 años'), ('De 11 a 15 años', 'De 11 a 15 años'), ('De 16 a 20 años', 'De 16 a 20 años'), ('De 21 a 25 años', 'De 21 a 25 años'), ('De 26 a 30 años', 'De 26 a 30 años'), ('Más de 30 años', 'Más de 30 años')], max_length=30)),
                ('genero', models.CharField(choices=[('', 'Selecciona un género'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('No binario', 'No binario'), ('No especificado', 'Prefiero no decirlo')], max_length=30)),
                ('denuncia', models.CharField(max_length=10000)),
                ('testimonio_fecha', models.DateTimeField(auto_now_add=True)),
                ('ip_publica_testimonio', models.CharField(default='127.0.0.1', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DenunciaPublicada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denuncia', models.CharField(max_length=10000)),
            ],
        ),
    ]
