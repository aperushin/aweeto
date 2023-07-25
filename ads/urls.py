from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.views.ad import AdViewSet, AdImageView
from ads.views.cat import CategoryViewSet
from ads.views.selection import SelectionViewSet

router = SimpleRouter()
router.register('cat', CategoryViewSet)
router.register('ad', AdViewSet)
router.register('selection', SelectionViewSet)

urlpatterns = [
    path('ad/<int:pk>/upload_image/', AdImageView.as_view()),
]

urlpatterns += router.urls
