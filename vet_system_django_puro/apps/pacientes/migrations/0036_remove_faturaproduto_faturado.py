# Generated by Django 3.1.5 on 2021-01-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0035_auto_20210120_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faturaproduto',
            name='faturado',
        ),
    ]
