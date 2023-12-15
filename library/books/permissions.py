from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    
   def has_permission(self, request, view):

       if request.method in permissions.SAFE_METHODS and request.user:
           return True

       return request.user.is_staff