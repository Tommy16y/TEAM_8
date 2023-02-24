from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth import get_user_model
from applications.hotels.models import Hotels

User = get_user_model()

class Like(models.Model):
    owner = models
    comment = models
    is_like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.owner} liked -{self.comment.title}'


class Rating(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='retings'
    )
    Hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)    
        ],
        blank=True, null=True
    )
    def __str__(self):
        return f'{self.owner}'