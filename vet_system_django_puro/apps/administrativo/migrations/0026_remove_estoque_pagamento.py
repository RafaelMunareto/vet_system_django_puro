# Generated by Django 3.1.5 on 2021-01-21 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0025_auto_20210121_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='pagamento',
        ),
    ]
