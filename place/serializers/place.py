from rest_framework import serializers

from place.models import Place
from user.models import User


class PlaceSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )

    class Meta:
        model = Place
        fields = "__all__"
        read_only = ["created_at", "uuid"]
