from rest_framework import generics
from user.serializers import UserCreationSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreationSerializer
