from django.urls import path, include
from applications.rooms.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',HotelRoomViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('add/image/',CreateImageAPIView.as_view())
]