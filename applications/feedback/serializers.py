from rest_framework import serializers
from applications.feedback.models import CommentLike



class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLike
        fields = '__all__'

