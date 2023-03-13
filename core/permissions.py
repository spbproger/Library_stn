from rest_framework.permissions import BasePermission, IsAdminUser


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if (
            handler
            and self.permission_classes_per_method
            and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class PermissionAdminOrOwner(IsAdminUser):
    message = 'Информация только для Администратора или Владельца учетной записи'

    def has_permission(self, request, view):
        return bool(request.user.id == int(view.kwargs.get('pk'))
                    or
                    request.user.is_staff)
