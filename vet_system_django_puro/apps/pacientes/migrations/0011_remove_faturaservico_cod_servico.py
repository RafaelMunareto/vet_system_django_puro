# Generated by Django 3.1.4 on 2021-01-17 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_auto_20210117_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faturaservico',
            name='cod_servico',
        ),
    ]
