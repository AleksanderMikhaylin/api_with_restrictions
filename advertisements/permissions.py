from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True

        return obj.creator == request.user
