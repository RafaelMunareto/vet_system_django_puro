# Generated by Django 3.1.4 on 2021-01-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0046_auto_20210124_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescricao',
            old_name='descricao',
            new_name='prescricao',
        ),
    ]