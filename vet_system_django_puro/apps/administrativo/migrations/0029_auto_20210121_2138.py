# Generated by Django 3.1.4 on 2021-01-22 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0028_auto_20210121_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamentos',
            name='pagamento',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
