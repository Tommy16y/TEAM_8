# Generated by Django 4.1.7 on 2023-02-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_hotelrooms_category_hotelrooms_price_delete_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelrooms',
            old_name='category',
            new_name='category1',
        ),
    ]
