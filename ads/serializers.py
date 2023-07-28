from rest_framework import serializers

from ads.models import Ad, Category, AdSelection
from ads.validators import is_false


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
    is_published = serializers.BooleanField(validators=[is_false])

    class Meta:
        model = Ad
        exclude = ['image']

    def is_valid(self, raise_exception=False):
        self.initial_data['author'] = self.initial_data.pop('author_id', None)
        self.initial_data['category'] = self.initial_data.pop('category_id', None)
        return super().is_valid(raise_exception=raise_exception)


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'

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


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdSelection
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdDetailSerializer(many=True)

    class Meta:
        model = AdSelection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdSelection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AdSelection
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
