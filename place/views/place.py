from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from place.models import Place
from place.serializers import PlaceSerializer


class PlaceListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    model = Place
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def get(self, request, format=None):
        user = request.user
        if not user:
            return PermissionError()
        queryset = self.get_queryset().filter(members__user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
