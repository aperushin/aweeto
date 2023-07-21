from django_filters import rest_framework as filters

from ads.models import Ad


class AdFilterSet(filters.FilterSet):
    cat = filters.NumberFilter(field_name='category_id')
    text = filters.CharFilter(field_name='name', lookup_expr='icontains')
    location = filters.CharFilter(field_name='author__location__name', lookup_expr='icontains')
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Ad
        fields = ['cat', 'text', 'location', 'price_from', 'price_to']
