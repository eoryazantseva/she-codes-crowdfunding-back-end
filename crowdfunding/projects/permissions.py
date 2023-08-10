from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):  # We are making a class to represent our permission. It is based on the permissions.BasePermission class that DRF provides.
    def has_object_permission(self, request, view, obj): # we create a new function has_object_permissions. Permissions use this function to determine whether ornot a user has permission to access a model instance.
        if request.method in permissions.SAFE_METHODS:  # we check if the action the user wants to perform is listed in DRF's list of SAFE_METHODS. For our purposes this is really just a check to see if the user ismaking a GET request.
            return True  # If the user is making a GET request, we return TRUE - they do have permission! This ends the method.
        return obj.owner == request.user # the user us making a POST, PUT, PATCH or DELETE request. In this case, we return a boolean value (wether or not the user making the request is the same as the user saved in the owner field). It they match (TRUE) , they will be given permission
