from place.models import Answer
from rest_framework import serializers
from user.models import User


class AnswerSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.object.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )

    class Meta:
        model = Answer
        fields = "__all__"
        read_only = ["created_at", "uuid"]
