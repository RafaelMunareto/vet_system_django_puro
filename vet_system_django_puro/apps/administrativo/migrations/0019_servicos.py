# Generated by Django 3.1.5 on 2021-01-15 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0018_produtos_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=200)),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('venda', models.CharField(blank=True, max_length=100)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Servicos',
                'verbose_name_plural': 'Servicos',
                'ordering': ['id'],
            },
        ),
    ]