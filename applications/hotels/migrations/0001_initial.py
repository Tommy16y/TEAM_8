# Generated by Django 4.1.7 on 2023-02-22 11:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('stars', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotels.hotels')),
            ],
        ),
    ]
