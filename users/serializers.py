from rest_framework import serializers

from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True)
    total_ads = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'age', 'location', 'total_ads']


class UserDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'age', 'location']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'email', 'last_name', 'role', 'location', 'birth_date']

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'role', 'age', 'location']

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations', list())
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        if self._locations:
            user.location.clear()
            for location in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=location)
                user.location.add(location_obj)

            user.save()
        return user
