# Generated by Django 3.1.5 on 2021-01-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0027_pagamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamentos',
            name='pagamento',
            field=models.DateField(blank=True),
        ),
    ]