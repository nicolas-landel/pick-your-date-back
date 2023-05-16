from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from place.permissions import IsMemberPlace
from user.models import User
from user.serializers import UserFullDataSerializer


class GetUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserFullDataSerializer


class ListUserMembers(GenericAPIView):
    permission_classes = [IsAuthenticated, IsMemberPlace]
    queryset = User.objects.all()
    serializer_class = UserFullDataSerializer

    def get(self, request, *args, **kwargs):
        place_uuid = request.query_params.get("place")
        queryset = self.get_queryset().filter(members__place__uuid=place_uuid)
        return Response(self.get_serializer(queryset, many=True).data)
