from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserFullDataSerializer


class GetUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserFullDataSerializer
