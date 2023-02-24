from django.db import models
from applications.rooms.models import HotelRooms
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # hotel = models.ForeignKey(HotelRooms,on_delete=models.CASCADE,related_name='hotels')
    room = models.ForeignKey(HotelRooms, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_guests = models.IntegerField()
    is_confirmed = models.BooleanField(default=False)
    total_price = models.IntegerField(default = 0)

    def __str__(self):
        return f"({self.check_in_date} to {self.check_out_date})"


    # def create_total_price(self):
    #     a = HotelRooms.objects.get(id = self.room)
    #     self.totalprice = a.price*3


        

        


    