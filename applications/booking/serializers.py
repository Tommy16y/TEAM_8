from rest_framework import serializers
from .models import Booking
from django.contrib.auth import get_user_model
from applications.account.send_email import send_activation_code2
User = get_user_model()

class BookingSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%Y-%m-%d')
    check_out_date = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date', 'num_of_guests', 'is_confirmed')
        read_only_fields = ('id','user')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        user = validated_data['user']
        user.create_activation_code()
        send_activation_code2(user.email,user.activation_code )
        user.save()
        print('все ок')



        
        return super().create(validated_data)
