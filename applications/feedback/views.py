from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from applications.feedback.models import Favorite,Rating
from applications.feedback.serializers import FavoriteSerializer,RatingSerializer,RatinggSeriazlier
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins,generics, viewsets
from applications.hotels.models import Hotels
from django.db.models import Avg


# class CommentLikeModelViewSet(ModelViewSet):
#     queryset = CommentLike.objects.all()
#     serializer_class = CommentLikeSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner =self.request.user)



class RatingModelViewSet(mixins.ListModelMixin,GenericViewSet,mixins.CreateModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     return super().perform_create(owner = self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner = self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner =self.request.user)



class FavoriteViewSet(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,   
               GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(owner = self.request.user)
    #     return queryset
    

# class RatingList(generics.ListAPIView):
#     serializer_class = RatinggSeriazlier
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         return Rating.objects.annotate(avg_rating=Avg('rating')).filter(avg_rating__gt=5)
    

