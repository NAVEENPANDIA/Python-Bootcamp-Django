from django.contrib.auth import get_user_model
from rest_framework import permissions
from myapp.models import *
from rest_framework.permissions import BasePermission

User = get_user_model()


class IsUserOrIsAdmin(BasePermission):
    """Allow access to the respective User object and to admin users."""

    # def has_object_permission(self, request, view, obj):
    #     return (request.user and request.user.is_staff) or (
    #         isinstance(obj, User) and request.user == obj
    #     )

    def has_object_permission(self, request, view, obj):
        return (
           # staff can do everything
           (request.user and request.user.is_staff) or 
           # accessed obj is a Booking and belongs to the user
           (isinstance(obj, Booking) and request.user.pk == obj.user.pk) or 
           # user can access or modify his user object
           (isinstance(obj, User) and request.user.pk == obj.pk)
        )


class IsUserOrIsAdminPassenger(BasePermission):
    """Allow access to the respective User object and to admin users."""

    # def has_object_permission(self, request, view, obj):
    #     return (request.user and request.user.is_staff) or (
    #         isinstance(obj, User) and request.user == obj
    #     )

    def has_object_permission(self, request, view, obj):
        return (
           # staff can do everything
           (request.user and request.user.is_staff) or 
           # accessed obj is a Passenger and belongs to the user
           (isinstance(obj, Passenger) and request.user.pk == obj.user.pk) or 
           # user can access or modify his user object
           (isinstance(obj, User) and request.user.pk == obj.pk)
        )




 
 
