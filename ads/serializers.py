from rest_framework import serializers

from ads.models import Location, Ad, Category


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'author_id', 'price']


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price', 'description', 'is_published', 'category']

    def is_valid(self, raise_exception=False):
        self.initial_data['author'] = self.initial_data.pop('author_id')
        self.initial_data['category'] = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price', 'description', 'is_published', 'category', 'image']

    def is_valid(self, raise_exception=False):
        if 'author_id' in self.initial_data:
            self.initial_data['author'] = self.initial_data.pop('author_id')
        if 'category_id' in self.initial_data:
            self.initial_data['category'] = self.initial_data.pop('category_id')

        return super().is_valid(raise_exception=raise_exception)


class AdUpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image']

    def to_representation(self, instance):
        serializer = AdDetailSerializer(instance)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
