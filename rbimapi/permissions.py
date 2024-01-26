from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rbim.models import Users
import constants

class IsSuperadminAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user = Users.objects.filter(id = request.user.id).first()
        if not user:
            raise PermissionDenied({"auth-end":constants.AUTH_END_ERROR_MSG})
        if (user.role == "superadmin"): 
            return True
        raise PermissionDenied({"auth-end":constants.SADMIN_AUTH_END_ERROR_MSG})

class IsBarangayAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user = Users.objects.filter(id = request.user.id).first()
        if not user:
            raise PermissionDenied({"auth-end":constants.AUTH_END_ERROR_MSG})
        if (user.role == "barangay"): 
            return True
        raise PermissionDenied({"auth-end":constants.SADMIN_AUTH_END_ERROR_MSG})

class IsSuperAdminandBarangayAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user = Users.objects.filter(id = request.user.id).first()
        if not user:
            raise PermissionDenied({"auth-end":constants.AUTH_END_ERROR_MSG})
        if (user.role == "barangay") or (user.role == "superadmin"): 
            return True
        raise PermissionDenied({"auth-end":constants.SADMIN_AUTH_END_ERROR_MSG})
