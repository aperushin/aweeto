from django.urls import path
from rest_framework.routers import SimpleRouter

from ads import views

router = SimpleRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', views.index),
    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdImageView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
]

urlpatterns += router.urls
