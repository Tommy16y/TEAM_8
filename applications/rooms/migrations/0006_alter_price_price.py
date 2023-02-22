# Generated by Django 4.1.7 on 2023-02-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(choices=[('lux', '200'), ('pollux', '150'), ('standart', '100')], decimal_places=5, default=0, max_digits=5, max_length=30),
        ),
    ]