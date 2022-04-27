from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrWriteOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True


class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True


class IsUserOrWriteOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.usuario_solicitud == request.user
