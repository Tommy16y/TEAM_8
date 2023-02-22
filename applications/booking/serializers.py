from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%Y-%m-%d')
    check_out_date = serializers.DateField(format='%Y-%m-%d')
    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'check_in_date', 'check_out_date', 'num_of_guests', 'is_confirmed')
        read_only_fields = ('id','user')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)