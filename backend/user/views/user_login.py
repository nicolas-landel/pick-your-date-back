from django.contrib.auth import login
from rest_framework import permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user.serializers import UserFullDataSerializer, UserLoginSerializer


class UserLoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = UserLoginSerializer(
                data=self.request.data, context={"request": self.request}
            )
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            context = UserFullDataSerializer(user).data
            context["token"] = token.key

            return Response(
                context,
                status=status.HTTP_202_ACCEPTED,
                content_type="application/json",
            )
        except Exception:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
