from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsOwner(BasePermission):
    message = 'You are not the owner of this element'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return request.user == obj.owner

        if hasattr(obj, 'author'):
            return request.user == obj.author

        raise Exception('The model does not have the owner field')


class IsStaff(BasePermission):
    message = "You are not an admin or a moderator"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]
