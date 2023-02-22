from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.
from applications.hotels.models import Hotels
from applications.hotels.serializer import HotelSerializer,DeitalHotelSerializer
from applications.hotels.permissions import  IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter ,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class CustomPagination(PageNumberPagination):
    page_size = 3 
    page_size_query_param = 'page_size'
    max_page_size = 10000


# class HotelModelViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):

#     queryset = Hotels.objects.all()
#     serializer_class = 
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         return serializer.save(owner = self.request.user)


class HotelModelViewSet(mixins.ListModelMixin,GenericViewSet):

    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrReadOnly]
    

    pagination_class =CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    fillterset_fields = ['adress','stars',]
    search_fields = ['name',]
    ordering_fields = ['id','name',]

    
        


class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = DeitalHotelSerializer
    lookup_field = 'id'


    

    

    

