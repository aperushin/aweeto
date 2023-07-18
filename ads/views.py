import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView

from ads.models import Ad, Category, User


def index(request):
    return JsonResponse({'status': 'ok'})


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for ad in self.object_list:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author_id': ad.author_id,
                'price': ad.price,
            })

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data['name'],
            price=ad_data['price'],
            author=get_object_or_404(User, pk=ad_data['author_id']),
            description=ad_data['description'],
            is_published=ad_data['is_published'],
        )

        ad.category = get_object_or_404(Category, pk=ad_data['category_id'])
        ad.save()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author_id': ad.author_id,
            'price': ad.price,
            'description': ad.description,
            'is_published': ad.is_published,
        })


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
            'image': ad.image,
        })


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

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


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })
