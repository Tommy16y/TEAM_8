# Generated by Django 4.1.7 on 2023-02-23 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Классификация номера')),
            ],
        ),
        migrations.CreateModel(
            name='HotelRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Номер')),
                ('description', models.TextField(verbose_name='Описание номера')),
                ('busy', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='rooms.category')),
                ('hotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotels.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_images')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.hotelrooms')),
            ],
        ),
    ]
