from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Hotels(models.Model):
    
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    description = models.TextField()
    # image = models.ImageField(upload_to='images',blank=True,null=True)
    stars = models.SmallIntegerField(validators=[MinValueValidator(3), MaxValueValidator(5)],default=3)

    def __str__(self):
        return f'{self.name}'

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return f'{self.image}'


class Comment(models.Model):
    owner =  models.ForeignKey(User , on_delete=models.CASCADE, related_name='users')
    hotel =  models.ForeignKey(Hotels , on_delete=models.CASCADE, related_name= 'hotels')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.owner} -> {self.hotel.name}'






