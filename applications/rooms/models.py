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
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',default=None)
    title = models.CharField('Номер',max_length=50)
    description = models.TextField('Описание номера')
    busy = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='hotels',default= None)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    # image = models.ImageField(upload_to='images')
    # price = models.Choices(PRICE_ROOM)


    def __str__(self):
        return f'{self.title}'


# class Price(models.Model):
#     PRICE_ROOM = (
#     ('lux', 200),
#     ('pollux', 150),
#     ('standart',100)

#     )
    
#     price = models.CharField(max_length=20,choices=PRICE_ROOM,default=0)
#     room = models.ForeignKey(HotelRooms,related_name='room_price',on_delete=models.CASCADE, default=None)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')

    # def __str__(self):
    #     return f'{self.price}'



    


class RoomImage(models.Model):
    room = models.ForeignKey(HotelRooms,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='room_images')

    def __str__(self) -> str:
        return f'{self.room.title}'







    
