from rest_framework import generics
from user.serializers import UserCreationSerializer

# TODO modify and define a POST to get token


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreationSerializer
