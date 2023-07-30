from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad
from ads.filtersets import AdFilterSet
from ads.permissions import IsStaff, IsOwner
from ads.serializers import (
    AdDetailSerializer,
    AdListSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdUpdateImageSerializer,
)


@extend_schema_view(
    list=extend_schema(description='Retrieve ad list', summary='Ad list'),
    retrieve=extend_schema(description='Retrieve an ad', summary='Ad'),
    create=extend_schema(description='Create an ad', summary='Ad creation'),
    update=extend_schema(description='Update an ad', summary='Ad update'),
    partial_update=extend_schema(description='Partially update an ad', summary='Ad partial update'),
    destroy=extend_schema(description='Delete an ad', summary='Ad deletion'),
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
    default_permissions = [IsOwner | IsStaff]
    permissions = {
        'list': [AllowAny],
        'retrieve': [IsAuthenticated],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permissions)
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-price')
        return super().list(request, *args, **kwargs)


@extend_schema(description='Upload an image for an ad', summary='Upload ad image')
class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer
    http_method_names = ['put']
