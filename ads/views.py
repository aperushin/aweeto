from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, AdSelection
from ads.filtersets import AdFilterSet
from ads.permissions import IsOwner, AdPermission
from ads.serializers import (
    CategorySerializer,
    AdListSerializer,
    AdDetailSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdUpdateImageSerializer,
    SelectionListSerializer,
    SelectionDetailSerializer,
    SelectionCreateSerializer,
    SelectionUpdateSerializer,
)


def index(request):
    return JsonResponse({'status': 'ok'})


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

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action == 'list':
            # Ad list can be accessed by unauthorized users
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [AdPermission]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-price')
        return super().list(request, *args, **kwargs)


class SelectionViewSet(ModelViewSet):
    queryset = AdSelection.objects.all()
    default_serializer = SelectionDetailSerializer
    serializer_classes = {
        'list': SelectionListSerializer,
        'create': SelectionCreateSerializer,
        'update': SelectionUpdateSerializer,
        'partial_update': SelectionUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsOwner]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
