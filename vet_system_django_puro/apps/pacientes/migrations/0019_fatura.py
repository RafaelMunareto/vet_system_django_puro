# Generated by Django 3.1.5 on 2021-01-18 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('administrativo', '0019_servicos'),
        ('pacientes', '0018_remove_faturaproduto_cod_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.FloatField(blank=True, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.produtos')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
            options={
                'verbose_name': 'Fatura Produto',
                'verbose_name_plural': 'Fatura Produto',
                'ordering': ['id'],
            },
        ),
    ]
