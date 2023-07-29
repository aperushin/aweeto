from rest_framework import serializers

from ads.models import Ad, Category, AdSelection
from ads.validators import is_false
from users.models import UserRoles


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


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


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

    def is_valid(self, raise_exception=False):
        request = self.context.get('request')

        # Because it can seemingly randomly become Dict or immutable QueryDict
        self.initial_data = self.initial_data.copy()

        if request.user.role not in [UserRoles.ADMIN, UserRoles.MODERATOR] or 'owner' not in self.initial_data:
            self.initial_data['owner'] = request.user.id

        return super().is_valid(raise_exception=raise_exception)


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
