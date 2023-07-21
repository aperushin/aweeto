from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category
from ads.serializers import (
    CategorySerializer,
    AdListSerializer,
    AdDetailSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdUpdateImageSerializer,
)
from ads.filtersets import AdFilterSet


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

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.order_by('-price')
        return super().list(request, *args, **kwargs)


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
