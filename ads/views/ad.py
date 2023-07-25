from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from ads.models import Ad
from ads.filtersets import AdFilterSet
from ads.permissions import AdPermission
from ads.serializers import (
    AdDetailSerializer,
    AdListSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdUpdateImageSerializer,
)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilterSet
    default_serializer = AdDetailSerializer
    serializer_classes = {
        'list': AdListSerializer,
        'create': AdCreateSerializer,
        'update': AdUpdateSerializer,
        'partial_update': AdUpdateSerializer,
    }
    default_permissions = [AdPermission]
    permissions = {
        'list': [AllowAny],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permissions)
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-price')
        return super().list(request, *args, **kwargs)


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer
