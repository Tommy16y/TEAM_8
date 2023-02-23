from django.shortcuts import render
from applications.rooms.models import HotelRooms, RoomImage
from rest_framework.viewsets import ViewSet,ModelViewSet , GenericViewSet
from applications.rooms.serializers import HotelRoomsSerializer,RoomImageSerializer,DetailRoomSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated ,IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.viewsets import generics
from rest_framework  import mixins

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


# class HotelRoomViewSet(ModelViewSet):
#     queryset = HotelRooms.objects.all()
#     serializer_class = HotelRoomsSerializer
#     pagination_class = CustomPagination
    


    # def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)

        
class CreateImageAPIView(generics.CreateAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer 
    permission_classes = [IsAdminUser] 
        
    

class HotelDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = HotelRooms.objects.all()
    serializer_class = DetailRoomSerializer
    lookup_field = 'id'


class UserHotelRoomViewSet(mixins.ListModelMixin,GenericViewSet):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


# class AdminHotelRoomViewSet(ModelViewSet):
#     queryset = HotelRooms.objects.all()
#     serializer_class = HotelRoomsSerializer
#     pagination_class = CustomPagination
#     permission_classes = [IsAdminUser]


class AdminRoomsDeleteAPIView(generics.DestroyAPIView):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer






