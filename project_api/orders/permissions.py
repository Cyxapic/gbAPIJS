from rest_framework import permissions


class IsOrderOwner(permissions.BasePermission):
    """
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user and obj.user == request.user)
