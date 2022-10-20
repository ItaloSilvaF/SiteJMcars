# Generated by Django 4.0.6 on 2022-10-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_shop', models.CharField(default='About', max_length=50, verbose_name='Página')),
                ('titulo_shop', models.CharField(default=None, max_length=50, verbose_name='Título')),
                ('imagem_shop', models.ImageField(blank=True, null=True, upload_to='imagens_about/imagens_background', verbose_name='Background')),
                ('publicado_shop', models.BooleanField(default=False, verbose_name='Publicado')),
            ],
        ),
    ]
