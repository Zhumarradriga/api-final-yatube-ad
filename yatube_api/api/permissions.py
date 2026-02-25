from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем безопасные методы или если пользователь аутентифицирован
        return (request.method in permissions.SAFE_METHODS or 
                request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Читать могут все, изменять/удалять — только автор
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user