# Generated by Django 4.1.4 on 2023-03-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
    ]
