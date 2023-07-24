from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from avwto import settings
from users.views import LocationViewSet, UserViewSet
from ads.views import CategoryViewSet, AdViewSet

router = SimpleRouter()
router.register('location', LocationViewSet)
router.register('cat', CategoryViewSet)
router.register('ad', AdViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
