from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    # Permite consultar la insformacion solo si el metodo es GET
    def has_permission(self, request, view):
        # if request.method == 'GET':
        #     return True

        # Devuelve True si el usuario existe y tiene permiso de staff
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission

class SolicitudUserOrReadOnly(permissions.BasePermission):
    # Lectura global
    # Usuarios logueados creador de la informacion pueden crear o editar registros
    def has_object_permission(self, request, view, obj):
        # verificar si el metodo es GET, permite el acceso de solo lectura
        # if request.method in permissions.SAFE_METHODS:
        #     return  True
        # else:
        #     # regresar True para crear o modificar  si el usuario es el mismo que creo el registro
        #     return obj.usuario_solicitud == request.user

        # regresar True para crear o modificar  si el usuario es el mismo que creo el registro
        return obj.usuario_solicitud == request.user