# Generated by Django 3.1.4 on 2021-01-16 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_fatura_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatura',
            name='valor_produto',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fatura',
            name='valor_servico',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
