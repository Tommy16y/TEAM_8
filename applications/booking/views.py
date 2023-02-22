from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from applications.booking.models import Booking
from applications.booking.serializers import BookingSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from applications.booking.models import Booking
from rest_framework.response import Response
from applications.rooms.models import HotelRooms

User =get_user_model()

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class ConfirmView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            booking = Booking.objects.get(user = user)
            print(booking.room)
            room = HotelRooms.objects.get(title = booking.room)
            user.activation_code =''
            booking.is_confirmed = True
            room.busy = True
            booking.save()
            user.save()
            room.save()
            return Response('Ваша бронь потвердилась', status= 200)
        except User.DoesNotExist:
            return Response('Что-то пошло не так',status=400)