# Generated by Django 4.1.7 on 2023-02-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_alter_price_category_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.CharField(choices=[(200, 'lux'), (150, 'premium'), (100, 'standart')], default=0, max_length=30),
        ),
    ]