# Generated by Django 3.1.5 on 2021-01-21 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0023_remove_pagamentos_pagamento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pagamentos',
        ),
    ]
