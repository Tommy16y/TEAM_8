# Generated by Django 4.1.7 on 2023-02-24 05:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='stars',
            field=models.SmallIntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(5)]),
        ),
    ]