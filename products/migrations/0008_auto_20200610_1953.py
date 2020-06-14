# Generated by Django 3.0.7 on 2020-06-10 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200610_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=48, verbose_name='Número do Código de Barras')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='boleto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Produto', to='products.Boleto'),
        ),
    ]