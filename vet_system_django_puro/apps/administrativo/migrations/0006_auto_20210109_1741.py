# Generated by Django 3.1.4 on 2021-01-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_parceiros'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='agencia',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='banco',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='conta',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='obs',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
