from django.contrib.auth import authenticate
from rest_framework import serializers
from user.models import User


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )
            if not user:
                msg = "Access denied: wrong email or password."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserFullDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uuid", "email", "last_name", "first_name", "created_at"]
        read_only = ["created_at"]
