from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Читать могут все, изменять/удалять — только автор
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
