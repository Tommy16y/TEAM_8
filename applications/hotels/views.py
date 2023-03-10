from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet,ViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly , IsAdminUser
# Create your views here.
from applications.hotels.models import Hotels,Comment
from applications.hotels.serializer import HotelSerializer,DeitalHotelSerializer,CommentSerializer,HotelsSerializer
from applications.hotels.permissions import CanCreateBooking
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter ,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from applications.feedback.models import Rating
from django.db.models import Avg
from applications.feedback.serializers import RatinggSeriazlier
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

class CustomPagination(PageNumberPagination):
    page_size = 3 
    page_size_query_param = 'page_size'
    max_page_size = 10000


# class HotelModelViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):

#     queryset = Hotels.objects.all()
#     serializer_class = 
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         return serializer.save(owner = self.request.user)

@method_decorator(cache_page(120),name='dispatch')
class HotelModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,mixins.ListModelMixin,GenericViewSet):

    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [CanCreateBooking]
    

    pagination_class =CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    fillterset_fields = ['adress','stars',]
    search_fields = ['name',]
    ordering_fields = ['id','name',]







    
    
class HotelDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Hotels.objects.all()
    serializer_class = DeitalHotelSerializer
    lookup_field = 'id'



class CommentViewSet(ViewSet):
    def list(self,request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer      
    permission_classes = [IsAuthenticatedOrReadOnly]


    # @action(methods=['POST'],detail=True)  # lokalhost:8000/api/v1/post/15/like/
    # def like(self,request,pk, *args, **kwargs):
    #     user = request.user
    #     # print(user), '!!!!!!!!!'
    #     like_obj,_ = CommentLike.objects.get_or_create(owner=user,comment_id=pk)
    #     like_obj.is_like = not like_obj.is_like
    #     like_obj.save()
    #     status = 'liked'

    #     if not like_obj.is_like:
    #         status = 'unliked'
        

    #     return Response({'status': status})   


    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  


class RecommendedHotelsView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Hotels.objects.annotate(avg_rating=Avg('ratings__rating')).filter(avg_rating__gt=6)
        
        return queryset
