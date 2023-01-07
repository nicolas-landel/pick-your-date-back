from place.models import Comment
from rest_framework import serializers
from user.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.object.all(),
        pk_field=serializers.UUIDField(format="hex_verbose"),
        required=False,
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only = ["created_at", "uuid"]
