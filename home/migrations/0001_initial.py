# Generated by Django 4.1.5 on 2023-01-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_home', models.CharField(default='Home', max_length=50, verbose_name='Página')),
                ('titulo_home', models.CharField(default=None, max_length=7, verbose_name='Título')),
                ('subtitulo_home', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Subtítulo')),
                ('descricao_home', models.TextField(blank=True, default=None, max_length=35, null=True, verbose_name='Descrição')),
                ('publicado_home', models.BooleanField(default=False, verbose_name='Publicado')),
                ('imagem_home', models.ImageField(blank=True, default=None, null=True, upload_to='imagens_home', verbose_name='Background (1920x803)')),
                ('titulo_quadrado_grande_um', models.CharField(default=' ', max_length=50, verbose_name='Título 1 do quadrado grande ')),
                ('descricao_quadrado_grande_um', models.TextField(blank=True, default=None, max_length=100, null=True, verbose_name='Descrição 1 do quadrado grande ')),
                ('titulo_quadrado_grande_dois', models.CharField(default=' ', max_length=50, verbose_name='Título 2 do quadrado grande')),
                ('descricao_quadrado_grande_dois', models.TextField(blank=True, default=None, max_length=100, null=True, verbose_name='Descrição 2 do quadrado grande ')),
                ('titulo_quadrado_grande_tres', models.CharField(default=' ', max_length=50, verbose_name='Título 3 do quadrado grande')),
                ('descricao_quadrado_grande_tres', models.TextField(blank=True, default=None, max_length=100, null=True, verbose_name='Descrição 3 do quadrado grande ')),
            ],
            options={
                'verbose_name': 'Presonalização da página Home',
                'verbose_name_plural': 'Presonalização da página Home',
            },
        ),
    ]