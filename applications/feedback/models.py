from django.db import models
from django.contrib.auth import get_user_model
from applications.hotels.models import Comment

User = get_user_model()

class CommentLike(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='likes')
    is_like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.comment}'



     

