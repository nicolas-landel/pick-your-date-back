from place.models import Option
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("__all__",)
        read_only = ["created_at", "uuid"]
