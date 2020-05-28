# Generated by Django 2.2.6 on 2020-05-28 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200527_2049'),
        ('products', '0003_auto_20200528_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Produto', to='products.Produto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='User', to='users.User')),
            ],
        ),
    ]
