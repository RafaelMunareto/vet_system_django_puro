# Generated by Django 3.1.4 on 2021-01-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0012_auto_20210110_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
