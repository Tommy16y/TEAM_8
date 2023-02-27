from django.urls import path, include
from applications.hotels.views import *
from rest_framework.routers import DefaultRouter
from applications.feedback.views import *
from django.views.decorators.cache import cache_page


router = DefaultRouter()
router.register('comments',CommentModelViewSet)
router.register('',HotelModelViewSet)


urlpatterns = [
    path('', include (router.urls)),
    path('detail/<int:id>/', HotelDetailAPIView.as_view()),
    # path('recomended',HotelList.as_view()), 
]
