# Generated by Django 4.1 on 2022-08-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='sobrenome',
            field=models.CharField(max_length=150),
        ),
    ]
