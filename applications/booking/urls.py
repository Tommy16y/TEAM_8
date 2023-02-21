from django.urls import path, include
from rest_framework import routers
from .views import BookingViewSet

router = routers.DefaultRouter()
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]