# Generated by Django 4.1.7 on 2023-02-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=(('lux', '200'), ('pollux', '150'), ('standart', '100'))),
        ),
    ]
