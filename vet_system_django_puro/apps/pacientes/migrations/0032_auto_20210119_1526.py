# Generated by Django 3.1.5 on 2021-01-19 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0031_auto_20210119_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faturaproduto',
            name='faturado',
        ),
        migrations.RemoveField(
            model_name='faturaproduto',
            name='total',
        ),
        migrations.RemoveField(
            model_name='faturaservico',
            name='faturado',
        ),
        migrations.RemoveField(
            model_name='faturaservico',
            name='total',
        ),
    ]
