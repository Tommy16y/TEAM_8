from rest_framework import serializers
from applications.hotels.models import Hotels, HotelImage,Rating



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'