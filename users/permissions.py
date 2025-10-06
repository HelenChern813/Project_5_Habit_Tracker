from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
        return False


class IsUser(permissions.BasePermission):
    """Проверяет возможность редактирования привычек"""

    def has_object_permission(self, request, view, obj):

        if obj == request.user:
            return True
        return False
