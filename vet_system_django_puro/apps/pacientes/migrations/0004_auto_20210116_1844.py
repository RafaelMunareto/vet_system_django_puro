# Generated by Django 3.1.4 on 2021-01-16 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0019_servicos'),
        ('pacientes', '0003_fatura_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatura',
            name='produto',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='administrativo.produtos'),
        ),
        migrations.AlterField(
            model_name='fatura',
            name='servico',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='administrativo.servicos'),
        ),
    ]
