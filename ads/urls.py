from django.urls import path

from ads import views

urlpatterns = [
    path('', views.index),
    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
]
