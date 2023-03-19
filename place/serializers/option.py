from rest_framework import serializers

from place.models import Option
from user.models import User


class OptionSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )

    class Meta:
        model = Option
        fields = "__all__"
        read_only = ["created_at", "uuid"]
