import json

from ads.models import Location
from avwto.settings import TOTAL_ON_PAGE
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from users.models import User


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.prefetch_related('location').order_by('username')
        self.object_list = self.object_list.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))

        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_num = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_num)

        users = []
        for user in page_obj:
            users.append({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': [location.name for location in user.location.all()],
                'total_ads': user.total_ads,
            })

        response = {
            'items': users,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'role', 'age', 'location']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            username=user_data['username'],
            password=user_data['password'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            role=user_data['role'],
            age=user_data['age'],
        )

        for location in user_data['locations']:
            location_obj, created = Location.objects.get_or_create(
                name=location,
            )

            user.location.add(location_obj)

        return JsonResponse({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': [location.name for location in user.location.all()],
            })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'role', 'age', 'location']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        self.object.location.clear()

        for location in user_data['locations']:
            location_obj, created = Location.objects.get_or_create(
                name=location,
            )
            self.object.location.add(location_obj)

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'username': self.object.username,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'role': self.object.role,
            'age': self.object.age,
            'locations': [location.name for location in self.object.location.all()],
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': [location.name for location in user.location.all()],
            })
