from django.db.models import Count, Q
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import (
    UserCreateSerializer, UserListSerializer, UserUpdateSerializer, UserDetailSerializer, LocationSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    default_serializer = UserDetailSerializer
    serializer_classes = {
        'list': UserListSerializer,
        'create': UserCreateSerializer,
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))
        self.queryset = self.queryset.order_by('username')
        return super().list(request, *args, **kwargs)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
