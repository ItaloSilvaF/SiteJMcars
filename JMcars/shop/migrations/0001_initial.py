# Generated by Django 4.0.6 on 2022-10-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(default=None, max_length=50, verbose_name='Modelo')),
                ('marca', models.CharField(default=None, max_length=50, verbose_name='Marca')),
                ('ano', models.CharField(default=None, max_length=9, verbose_name='Ano')),
                ('cor', models.CharField(default=None, max_length=50, verbose_name='Cor')),
                ('quilometragem', models.CharField(default=None, max_length=50, verbose_name='Quilometragem')),
                ('motorizacao', models.CharField(default=None, max_length=50, verbose_name='Motorização')),
                ('cambio', models.CharField(default=None, max_length=50, verbose_name='Câmbio')),
                ('preco', models.CharField(default=None, max_length=50, verbose_name='Preço')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('imagem_um', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 1 (Capa)')),
                ('imagem_dois', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 2')),
                ('imagem_tres', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 3')),
                ('imagem_quatro', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 4')),
                ('imagem_cinco', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 4')),
                ('imagem_seis', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 6')),
                ('imagem_sete', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 7')),
                ('imagem_oito', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 8')),
                ('imagem_nove', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 9')),
                ('imagem_dez', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_carros/imagens_carro_<int:pk>', verbose_name='Imagem 10')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_shop', models.CharField(default='About', max_length=50, verbose_name='Página')),
                ('titulo_shop', models.CharField(default=None, max_length=50, verbose_name='Título')),
                ('imagem_shop', models.ImageField(blank=True, null=True, upload_to='imagens_shop/imagens_background', verbose_name='Background')),
                ('publicado_shop', models.BooleanField(default=False, verbose_name='Publicado')),
            ],
        ),
    ]
