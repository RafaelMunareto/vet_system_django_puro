# Generated by Django 3.1.4 on 2021-01-09 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0006_auto_20210109_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='cpf',
            new_name='cnpj',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='especialidade',
            new_name='ramo',
        ),
    ]
