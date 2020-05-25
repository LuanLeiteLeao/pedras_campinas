# Generated by Django 2.2.7 on 2020-05-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome Do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Preço em R$')),
                ('categoria', models.CharField(choices=[[0, 'Quartzo'], [1, 'Seixo'], [2, 'Laje'], [3, 'Retalho'], [4, 'Serrada']], max_length=1, null=True, verbose_name='Categoria')),
                ('cor', models.CharField(choices=[[0, 'Rosa'], [1, 'Branco'], [2, 'Verde']], max_length=1, null=True, verbose_name='Cor')),
                ('tamanho_em_cm', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Tamanho em cm')),
                ('imagem', models.ImageField(upload_to='mangueiras/imagens/', verbose_name='Imagem do Produto')),
            ],
        ),
    ]
