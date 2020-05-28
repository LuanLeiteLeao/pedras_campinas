# Generated by Django 2.2.6 on 2020-05-27 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200312_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='data_de_nascimento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
    ]
