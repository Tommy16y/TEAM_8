from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model
from applications.hotels.models import Comment,Hotels
from django.core.validators import MinValueValidator,MaxValueValidator

User = get_user_model()

class CommentLike(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='likes')
    is_like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.comment}'



     

class Rating(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='retings'
    )
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)    
        ]
    )

    def str(self):
        return f'{self.owner}'
     
class Favorite(models.Model):
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )