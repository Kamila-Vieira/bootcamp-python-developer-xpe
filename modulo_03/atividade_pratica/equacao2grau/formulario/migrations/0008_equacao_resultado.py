# Generated by Django 4.1.3 on 2022-11-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0007_remove_equacao_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='equacao',
            name='resultado',
            field=models.CharField(max_length=300, null=True, verbose_name='resultado'),
        ),
    ]