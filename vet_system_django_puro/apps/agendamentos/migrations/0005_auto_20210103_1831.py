# Generated by Django 3.1.4 on 2021-01-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0004_auto_20210103_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentos',
            name='tipo',
            field=models.IntegerField(),
        ),
    ]
