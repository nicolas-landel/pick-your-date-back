from rest_framework.permissions import BasePermission

from user.models import Membership


class IsMemberPlace(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        place = request.place
        return Membership.objects.filter(place=place, user=user).exists()
