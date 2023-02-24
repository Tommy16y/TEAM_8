from django.urls import path, include
from applications.rooms.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',UserHotelRoomViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('add/image/',CreateImageAPIView.as_view()),
    path('<int:id>/',HotelDetailAPIView.as_view()),
    path('admin/<int:pk>/',AdminRoomsDeleteAPIView.as_view()),

]