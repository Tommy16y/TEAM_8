# Generated by Django 4.1.7 on 2023-02-22 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_delete_comment'),
        ('rooms', '0006_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelrooms',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotels.hotels'),
        ),
    ]