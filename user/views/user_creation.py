from django.contrib.auth import login
from rest_framework import permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from core.errors_handler import custom_exception_handler
from user.serializers import UserCreationSerializer, UserFullDataSerializer


class UserCreateView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    context = {}
    serializer_class = UserCreationSerializer

    def post(self, request, format=None):
        try:
            serializer = UserCreationSerializer(
                data=self.request.data, context={"request": self.request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = serializer.instance
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            self.context["user"] = UserFullDataSerializer(user).data
            self.context["token"] = token.key

            return Response(
                self.context,
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )
        except Exception as e:
            return custom_exception_handler(e, self.context)
