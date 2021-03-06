# Generated by Django 3.1.4 on 2021-01-17 01:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('pacientes', '0008_auto_20210116_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaturaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_produto', models.IntegerField(blank=True, null=True)),
                ('produto', models.CharField(blank=True, max_length=200)),
                ('qtd_produto', models.FloatField(blank=True, null=True)),
                ('valor_produto', models.FloatField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
            options={
                'verbose_name': 'Fatura Produto',
                'verbose_name_plural': 'Fatura Produto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FaturaServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_servico', models.IntegerField(blank=True, null=True)),
                ('servico', models.CharField(blank=True, max_length=200)),
                ('qtd_servico', models.FloatField(blank=True, null=True)),
                ('valor_servico', models.FloatField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
            options={
                'verbose_name': 'Fatura Servi??o',
                'verbose_name_plural': 'Fatura Servi??o',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Fatura',
        ),
    ]
