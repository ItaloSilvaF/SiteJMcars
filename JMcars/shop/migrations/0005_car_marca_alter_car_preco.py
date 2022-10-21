# Generated by Django 4.0.6 on 2022-10-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_car_ano_car_cambio_car_cor_car_motorizacao_car_preco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='marca',
            field=models.CharField(default=None, max_length=50, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='preco',
            field=models.FloatField(default=None, max_length=50, verbose_name='Preço'),
        ),
    ]
