# Generated by Django 3.1.4 on 2021-01-13 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0016_auto_20210112_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='qtd',
            new_name='qtd_total',
        ),
        migrations.RenameField(
            model_name='estoque',
            old_name='valor',
            new_name='valor_total',
        ),
    ]