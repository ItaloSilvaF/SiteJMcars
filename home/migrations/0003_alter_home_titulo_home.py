# Generated by Django 4.1.5 on 2023-01-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_home_titulo_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='titulo_home',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Título'),
        ),
    ]
