from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import User
from rest_framework.views import View


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj: User):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user 