from rest_framework import serializers

from place.models import Answer, Option, Place
from user.models import User


class AnswerSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )
    option = serializers.PrimaryKeyRelatedField(
        queryset=Option.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Answer
        fields = "__all__"
        read_only = ["created_at", "uuid"]
