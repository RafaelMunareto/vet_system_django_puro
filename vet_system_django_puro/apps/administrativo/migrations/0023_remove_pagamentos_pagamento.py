# Generated by Django 3.1.5 on 2021-01-21 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0022_pagamentos_pagamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagamentos',
            name='pagamento',
        ),
    ]