from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, LocationViewSet


router = SimpleRouter()
router.register('user', UserViewSet)
router.register('location', LocationViewSet)

urlpatterns = [

]

urlpatterns += router.urls
