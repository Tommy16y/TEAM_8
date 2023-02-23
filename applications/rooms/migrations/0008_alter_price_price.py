# Generated by Django 4.1.7 on 2023-02-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_hotelrooms_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(choices=[('200', 'lux'), ('150', 'premium'), ('100', 'standart')], decimal_places=5, default=0, max_digits=5, max_length=30),
        ),
    ]