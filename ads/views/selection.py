from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ads.models import AdSelection
from ads.permissions import IsOwner
from ads.serializers import (
    SelectionListSerializer,
    SelectionDetailSerializer,
    SelectionCreateSerializer,
    SelectionUpdateSerializer,
)


class SelectionViewSet(ModelViewSet):
    queryset = AdSelection.objects.all()
    default_serializer = SelectionDetailSerializer
    serializer_classes = {
        'list': SelectionListSerializer,
        'create': SelectionCreateSerializer,
        'update': SelectionUpdateSerializer,
        'partial_update': SelectionUpdateSerializer,
    }
    default_permissions = [IsOwner]
    permissions = {
        'retrieve': [AllowAny],
        'list': [AllowAny],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permissions)
        return super().get_permissions()
