# Generated by Django 4.0.6 on 2022-10-26 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_car_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='categoria',
            new_name='categoria_carro',
        ),
    ]