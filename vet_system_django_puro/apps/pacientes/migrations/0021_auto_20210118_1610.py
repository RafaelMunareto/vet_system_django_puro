# Generated by Django 3.1.5 on 2021-01-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0020_auto_20210118_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicofatura',
            name='paciente',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='historicofatura',
            name='produto',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='historicofatura',
            name='servico',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='historicofatura',
            name='tutor',
            field=models.CharField(max_length=200),
        ),
    ]