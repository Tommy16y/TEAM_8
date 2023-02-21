from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    category = models.CharField('Классификация номера',max_length=50)

    def __str__(self):
        return f'{self.category}'
        


class HotelRooms(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    title = models.CharField('Номер',max_length=50)
    description = models.TextField('Описание номера')
    busy = models.BooleanField(default=True)
    hotel = models.ForeignKey
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title}'


class RoomImage(models.Model):
    room = models.ForeignKey(HotelRooms,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='room_images')

    def __str__(self) -> str:
        return f'{self.room.title}'







    
