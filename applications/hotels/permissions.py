
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    
    def admin_or_no(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        
        return request.user.is_admi_user
    
    