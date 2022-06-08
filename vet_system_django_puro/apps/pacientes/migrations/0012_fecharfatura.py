# Generated by Django 3.1.5 on 2021-01-18 12:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('administrativo', '0019_servicos'),
        ('pacientes', '0011_remove_faturaservico_cod_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='FecharFatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_servico', models.FloatField(blank=True, null=True)),
                ('valor_servico', models.FloatField(blank=True, null=True)),
                ('qtd_produto', models.FloatField(blank=True, null=True)),
                ('valor_produto', models.FloatField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.servicos')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
            options={
                'verbose_name': 'Fechar Fatura',
                'verbose_name_plural': 'Fechar Fatura',
                'ordering': ['id'],
            },
        ),
    ]