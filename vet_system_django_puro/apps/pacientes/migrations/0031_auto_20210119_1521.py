# Generated by Django 3.1.5 on 2021-01-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0030_faturaservico_faturado'),
    ]

    operations = [
        migrations.AddField(
            model_name='faturaproduto',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faturaservico',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
