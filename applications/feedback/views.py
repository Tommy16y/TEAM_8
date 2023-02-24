from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from applications.feedback.models import CommentLike
from applications.feedback.serializers import CommentLikeSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class CommentLikeModelViewSet(ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

  