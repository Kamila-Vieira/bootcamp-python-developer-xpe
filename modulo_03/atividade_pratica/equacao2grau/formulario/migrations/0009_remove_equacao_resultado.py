# Generated by Django 4.1.3 on 2022-11-27 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0008_equacao_resultado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equacao',
            name='resultado',
        ),
    ]
