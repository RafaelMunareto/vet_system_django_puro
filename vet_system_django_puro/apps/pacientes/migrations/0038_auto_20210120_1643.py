# Generated by Django 3.1.5 on 2021-01-20 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0037_auto_20210120_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faturaproduto',
            name='data_cadastro',
            field=models.DateField(blank=True, default=datetime.datetime.today),
        ),
    ]
