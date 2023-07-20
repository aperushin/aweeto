from rest_framework import serializers

from ads.models import Location, Ad, Category


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'author_id', 'price']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
