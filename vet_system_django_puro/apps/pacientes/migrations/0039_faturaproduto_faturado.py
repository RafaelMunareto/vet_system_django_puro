# Generated by Django 3.1.5 on 2021-01-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0038_auto_20210120_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturaproduto',
            name='faturado',
            field=models.IntegerField(default=0),
        ),
    ]
