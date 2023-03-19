from rest_framework.permissions import BasePermission

from place.models import Place
from user.models import Membership


class IsMemberPlace(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        place_uuid = request.query_params.get("place")
        if not Place.objects.filter(uuid=place_uuid).exists():
            return False
        return Membership.objects.filter(place__uuid=place_uuid, user=user).exists()
