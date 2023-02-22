from django.urls import path, include
from applications.hotels.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',HotelModelViewSet)

urlpatterns = [
    path('hotels/',include(router.urls)),
    path('hotels/<int:id>/', HotelDetailAPIView.as_view()),
]