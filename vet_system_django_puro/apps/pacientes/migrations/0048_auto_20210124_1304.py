# Generated by Django 3.1.4 on 2021-01-24 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0047_auto_20210124_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescricao',
            name='data_cadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]