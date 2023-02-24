from rest_framework import serializers
from .models import Booking
from django.contrib.auth import get_user_model
from applications.rooms.models import HotelRooms
from rest_framework.response import Response
from applications.account.send_email import send_activation_code2
User = get_user_model()

class BookingSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%Y-%m-%d')
    check_out_date = serializers.DateField(format='%Y-%m-%d')
   

    # def validate(self, attrs):
    #     date = attrs.get('check_in_date')
    #     date2 = attrs.get('check_out_date')
    #     if date2 <date:
    #         raise('Неправильная дата')
    #     elif date2 == date:
    #         raise('У нас только по суточно')
    #     elif date>date:
    #         return attrs

        
    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date', 'num_of_guests', 'is_confirmed','total_price')
        read_only_fields = ('id','user','total_price')
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        if validated_data['room'].busy == True:
            raise('No')
        user = validated_data['user']
        d1 = validated_data['check_in_date']
        d2 = validated_data['check_out_date']
        day = self.dayss(d1=d1,d2=d2)
        room = validated_data['room']
        user.create_activation_code()
        total_price1 = self.create_total_price(room=room,day=day)
        validated_data['total_price']= total_price1
        send_activation_code2(user.email,user.activation_code )
        user.save()
        print('все ок')
        return super().create(validated_data)

    def create_total_price(self, room,day):
        a = HotelRooms.objects.get(title = room)
        c= a.price
        self.totalprice = c * int(day)
        return self.totalprice   

    def dayss(self,d1,d2):
        import datetime
        d2 = str(d2).split('-')
        d1 = str(d1).split('-')
        aa = datetime.date(int(d2[0]),int(d2[1]),int(d2[2]))
        bb = datetime.date(int(d1[0]),int(d1[1]),int(d1[2]))
        cc = aa-bb
        dd = str(cc)
        dd = (dd.split()[0])
        print(dd)
        return dd
