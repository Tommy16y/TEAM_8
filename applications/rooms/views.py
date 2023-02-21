from django.shortcuts import render
from applications.rooms.models import HotelRooms, RoomImage
from rest_framework.viewsets import ViewSet,ModelViewSet
from applications.rooms.serializers import HotelRoomsSerializer,RoomImageSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class HotelRoomViewSet(ModelViewSet):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer
    pagination_class = CustomPagination


    # def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)

        
class CreateImageAPIView(generics.CreateAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer 
    permission_classes = [IsAuthenticated] 
        
    







