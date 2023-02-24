from django.shortcuts import render
from applications.hotels.models import Hotels, Rating
from applications.hotels.serializer import HotelSerializer, RatingSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.
class RatingModelViewSet(mixins.ListModelMixin,GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]