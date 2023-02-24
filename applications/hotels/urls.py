from django.urls import path, include
from applications.hotels.views import *
from rest_framework.routers import DefaultRouter
from applications.feedback.views import *


router = DefaultRouter()
# router.register('',HotelModelViewSet)
router.register('comments',CommentModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('detail/<int:id>/', HotelDetailAPIView.as_view()),
]