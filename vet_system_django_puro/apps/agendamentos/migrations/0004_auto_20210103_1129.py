# Generated by Django 3.1.4 on 2021-01-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0003_auto_20210103_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentos',
            name='data',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='agendamentos',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
