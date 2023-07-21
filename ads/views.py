import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category, Location
from users.models import User
from ads.serializers import LocationSerializer, AdListSerializer
from ads.filtersets import AdFilterSet


def index(request):
    return JsonResponse({'status': 'ok'})


# Ad views


class AdListView(ListAPIView):
    queryset = Ad.objects.order_by('-price')
    serializer_class = AdListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilterSet


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        category = get_object_or_404(Category, pk=ad_data['category_id'])
        author = get_object_or_404(User, pk=ad_data['author_id'])

        ad = Ad.objects.create(
            name=ad_data['name'],
            price=ad_data['price'],
            author=author,
            description=ad_data['description'],
            is_published=ad_data['is_published'],
            category=category
        )

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author_id': ad.author_id,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category', 'image']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        if 'name' in ad_data:
            self.object.name = ad_data['name']
        if 'author_id' in ad_data:
            self.object.author_id = ad_data['author_id']
        if 'price' in ad_data:
            self.object.price = ad_data['price']
        if 'description' in ad_data:
            self.object.description = ad_data['description']
        if 'category_id' in ad_data:
            self.object.category_id = ad_data['category_id']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author_id,
            'price': self.object.price,
            'description': self.object.description,
            'category_id': self.object.category_id,
            'is_published': self.object.is_published,
            'image': str(self.object.image),
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author_id,
            'price': self.object.price,
            'description': self.object.description,
            'category_id': self.object.category_id,
            'is_published': self.object.is_published,
            'image': str(self.object.image),
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author_id': ad.author_id,
            'price': ad.price,
            'description': ad.description,
            'category_id': ad.category_id,
            'is_published': ad.is_published,
            'image': str(ad.image),
        })


# Category views


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')

        response = []
        for category in self.object_list:
            response.append({
                'id': category.id,
                'name': category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(name=category_data['name'])

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)

        self.object.name = category_data['name']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
