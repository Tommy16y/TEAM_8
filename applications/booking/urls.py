from django.urls import path, include
from rest_framework import routers
from applications.booking.views import AdminBookingViewSet,ConfirmView

router = routers.DefaultRouter()
router.register('', AdminBookingViewSet)

urlpatterns = [
    path('hotels/', include(router.urls)),
    path('activate/<uuid:activation_code>/', ConfirmView.as_view()),
]