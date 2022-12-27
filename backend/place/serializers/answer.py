from place.models import Answer
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("__all__",)
        read_only = ["created_at", "uuid"]
