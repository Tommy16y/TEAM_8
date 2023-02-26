from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import *
from applications.hotels.views import *

router = DefaultRouter()
# router.register('',CommentModelViewSet)
router.register('like',CommentLikeModelViewSet)
router.register('favorite',FavoriteViewSet)
router.register('rating',RatingModelViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('rec',RatingList.as_view(), name='hotel-list'),
    # path('like/<int:id>/',CommentLikeModelViewSet.as_view()),
    
    
]