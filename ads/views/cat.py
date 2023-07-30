from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema

from ads.models import Category
from ads.serializers import CategorySerializer


@extend_schema_view(
    list=extend_schema(description='Retrieve category list', summary='Category list'),
    retrieve=extend_schema(description='Retrieve a category', summary='Category'),
    create=extend_schema(description='Create a category', summary='Category creation'),
    update=extend_schema(description='Update a category', summary='Category update'),
    partial_update=extend_schema(description='Partially update a category', summary='Category partial update'),
    destroy=extend_schema(description='Delete a category', summary='Category deletion'),
)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
