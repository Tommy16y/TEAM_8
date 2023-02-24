from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import *
from applications.hotels.views import *

router = DefaultRouter()
# router.register('',CommentModelViewSet)
router.register('like',CommentLikeModelViewSet)


urlpatterns = [
    path('',include(router.urls)),
]