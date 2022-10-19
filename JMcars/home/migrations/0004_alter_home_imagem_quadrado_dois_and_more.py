# Generated by Django 4.1.2 on 2022-10-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_home_imagem_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='imagem_quadrado_dois',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_home/quadrado2', verbose_name='Imagem do quadrado 2 (400x250)'),
        ),
        migrations.AlterField(
            model_name='home',
            name='imagem_quadrado_tres',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_home/quadrado3', verbose_name='Imagem do quadrado 3 (400x250)'),
        ),
        migrations.AlterField(
            model_name='home',
            name='imagem_quadrado_um',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_home/quadrado1', verbose_name='Imagem do quadrado 1 (400x250)'),
        ),
    ]
