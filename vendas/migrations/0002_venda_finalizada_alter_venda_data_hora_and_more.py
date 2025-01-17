# Generated by Django 4.2.5 on 2024-01-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='venda',
            name='data_hora',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
