from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
    owner = models
    comment = models
    is_like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.owner} liked -{self.comment.title}'

