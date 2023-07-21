from django.urls import path

from ads import views

urlpatterns = [
    path('', views.index),
    path('ad/<int:pk>/upload_image/', views.AdImageView.as_view()),
]
