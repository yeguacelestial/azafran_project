# Generated by Django 3.0.6 on 2020-07-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azafran_denuncias', '0003_auto_20200727_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='ip_publica_testimonio',
            field=models.CharField(max_length=100),
        ),
    ]
