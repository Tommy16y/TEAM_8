from rest_framework import serializers
from applications.hotels.models import Hotels, HotelImage,Comment
from applications.rooms.serializers import HotelRoomsSerializer,HotelRoomSerializer
from applications.rooms.models import HotelRooms



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

    
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        # fields = '__all__'
        fields = ('image',)



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment 
        # fields = '__all__'       
        fields = ('owner','body','created_at',)

class DeitalHotelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
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
        comm =  instance.hotels.all()
        print(comm)
        b = []
        for i in comm:
            b.append(CommentSerializer(i).data)    
        qury = instance.rooms.all()
        qury = instance.rooms.filter(busy=False)
        a = []
        for i in qury:
            a.append(HotelRoomSerializer(i).data)
        representation['all_rooms'] = a
        representation['comments'] = b
        return representation


    