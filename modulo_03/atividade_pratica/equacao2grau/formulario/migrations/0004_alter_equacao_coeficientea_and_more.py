# Generated by Django 4.1.3 on 2022-11-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_remove_equacao_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equacao',
            name='coeficienteA',
            field=models.IntegerField(verbose_name='a'),
        ),
        migrations.AlterField(
            model_name='equacao',
            name='coeficienteB',
            field=models.IntegerField(verbose_name='b'),
        ),
        migrations.AlterField(
            model_name='equacao',
            name='coeficienteC',
            field=models.IntegerField(verbose_name='c'),
        ),
    ]
