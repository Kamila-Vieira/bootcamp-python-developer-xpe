# Generated by Django 4.1.3 on 2022-11-27 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_equacao_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equacao',
            name='result',
        ),
    ]