from django.urls import path, include
from applications.hotels.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',HotelModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('detail/<int:id>/', HotelDetailAPIView.as_view()),
]