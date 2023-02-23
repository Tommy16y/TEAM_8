from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanCreateBooking(BasePermission):
    
    def has_permission(self, request, view):
       
        if request.method == 'POST':
            return True

   
        if request.user.is_staff:
            return True

     
        return False

    def has_object_permission(self, request, view, obj):
      
        if request.user.is_staff:
            return True

        return False
