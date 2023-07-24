from rest_framework.permissions import BasePermission
from users.models import User, UserRoles


class IsOwner(BasePermission):
    message = ''

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
