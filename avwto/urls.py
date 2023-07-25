from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from avwto import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),
    path('', include('users.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
