from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    """
    Permission class for AdSelection model views
    """
    message = "Only the selection's owner can make changes"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class AdPermission(BasePermission):
    """
    Permission class for Ad model views

    Allows access only to authenticated users.
    Making changes also requires a moderator/admin role or being the ad's author
    """
    message = "Only the ad's owner or a moderator can make changes"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in SAFE_METHODS or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return request.user == obj.author
