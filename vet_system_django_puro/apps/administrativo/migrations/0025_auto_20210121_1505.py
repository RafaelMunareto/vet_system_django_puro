# Generated by Django 3.1.5 on 2021-01-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0024_delete_pagamentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='pagamento',
        ),
        migrations.AddField(
            model_name='estoque',
            name='pagamento',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]