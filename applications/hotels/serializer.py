from rest_framework import serializers
from applications.hotels.models import Hotels, HotelImage
from applications.rooms.serializers import HotelRoomsSerializer,HotelRoomSerializer
from applications.rooms.models import HotelRooms
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

    
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'
    

class DeitalHotelSerializer(serializers.ModelSerializer):
    # rooms = HotelRoomSerializer(many= True, read_only = True)
    class Meta:
        model = Hotels
        fields =  '__all__'
    
    
    # queryset = HotelRooms.objects.all()
    # for i in queryset:
    #     print(i.title)
    #     print(i.busy)
    #     print(i.description)
    #     print(i.hotel)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # queryset = HotelRooms.objects.all()
        qury = instance.rooms.all()
        qury = instance.rooms.filter(busy=False)
        a = []
        for i in qury:
            a.append(HotelRoomSerializer(i).data)
        representation['all_rooms'] = a
        return representation


    