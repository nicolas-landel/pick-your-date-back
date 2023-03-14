from rest_framework import serializers

from place.models import Answer, Comment
from user.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.object.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )
    answer = serializers.PrimaryKeyRelatedField(
        queryset=Answer.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    replied_to = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only = ["created_at", "uuid"]
