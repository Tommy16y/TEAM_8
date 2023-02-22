from rest_framework import serializers
from applications.rooms.models import HotelRooms,RoomImage


class RoomImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomImage
        fields = '__all__'

class HotelRoomsSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True,read_only=True)  


    class Meta:
        model = HotelRooms
        fields = '__all__'  




    def create(self,validated_data):
        room = HotelRooms.objects.create(**validated_data)
        request = self.context.get('request') 
        data = request.FILES
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(RoomImage(room=room,image=i))
        RoomImage.objects.bulk_create(image_objects) 
        return room          

class HotelRoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True,read_only=True)  
    class Meta:
        model = HotelRooms
        fields = '__all__'  

class DetailRoomSerializer(serializers.Serializer):
    rooms = HotelRoomSerializer(many=True,read_only = True)
    class Meta:
        model = HotelRooms
        fields = '__all__'


# class DeitalHotelSerializer(serializers.ModelSerializer):
#     # rooms = HotelRoomSerializer(many= True, read_only = True)
#     class Meta:
#         model = Hotels
#         fields =  '__all__'
    
    
