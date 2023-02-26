from rest_framework import serializers
from applications.feedback.models import CommentLike,Rating,Favorite



class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLike
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Rating
        fields = ('rating','hotel','owner')


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorite
        fields = '__all__'


class RatinggSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'