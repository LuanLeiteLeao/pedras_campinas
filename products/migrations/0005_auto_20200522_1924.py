# Generated by Django 2.2.7 on 2020-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200520_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[[0, 'Quartzo'], [1, 'Seixo'], [2, 'Laje'], [3, 'Retalho'], [4, 'Serrada']], max_length=1, null=True, verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome Do Produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Preço'),
        ),
    ]
