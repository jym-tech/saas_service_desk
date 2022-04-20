from rest_framework import permissions


class StaffOrWriteOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission


class UserOrReadOnly(permissions.BasePermission):
    metodos = ('PUT', 'POST', 'DELETE')

    def has_permission(self, request, view):
        if request.method not in self.metodos:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.usuario_solicitud == request.user:
            return True
        return False


class UserOrWriteOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.usuario_solicitud == request.user:
            return True
        return False
