from django.db import models
from applications.rooms.models import HotelRooms
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRooms, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_guests = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.check_in_date} to {self.check_out_date})"
