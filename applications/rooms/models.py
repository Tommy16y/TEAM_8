from django.db import models
from django.contrib.auth import get_user_model
from applications.hotels.models import Hotels

# PRICE_ROOM = [
#     ('lux', '200'),
#     ('pollux', '150'),
#     ('standart','100')

# ]

User = get_user_model()

class Category(models.Model):
    category = models.CharField('Классификация номера',max_length=50)

    def __str__(self):
        return f'{self.category}'
        

class HotelRooms(models.Model):
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    
    title = models.CharField('Номер',max_length=50)
    description = models.TextField('Описание номера')
    busy = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='rooms',default= None)
    # image = models.ImageField(upload_to='images')
    # price = models.Choices(PRICE_ROOM)


    def __str__(self):
        return f'{self.title}'


class Price(models.Model):
    # PRICE_ROOM = (
    # ('lux','200'),
    # ('premium','150'),
    # ('standart','100'),

    # )
    # choices=PRICE_ROOM,,.
    price = models.CharField(max_length=30,default=0)
    room = models.ForeignKey(HotelRooms,related_name='room_price',on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')



    


class RoomImage(models.Model):
    room = models.ForeignKey(HotelRooms,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='room_images')

    def __str__(self) -> str:
        return f'{self.room.title}'







    
