# Generated by Django 3.1.5 on 2021-01-21 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0019_servicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='fornecedor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='administrativo.fornecedores'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.fornecedores')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.produtos')),
            ],
            options={
                'verbose_name': 'Pagamentos',
                'verbose_name_plural': 'Pagamentos',
                'ordering': ['id'],
            },
        ),
    ]