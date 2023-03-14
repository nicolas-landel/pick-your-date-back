from rest_framework import serializers

from place.models import Place
from user.models import Membership, User


class MembershipSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.object.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Membership
        fields = "__all__"
