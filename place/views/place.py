from core.views import ListView
from place.models import Place
from place.serializers import PlaceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PlaceListView(ListView):
    permission_classes = [IsAuthenticated]
    model = Place
    serializer_class = PlaceSerializer
    serializer = PlaceSerializer
    queryset = Place.objects.all()

    def get(self, request, format=None):
        # user = request.user
        queryset = self.get_queryset()
        print("QQQQQ", queryset)
        serializer = self.serializer(queryset, many=True)
        print("SSSSS", serializer.data)
        return Response(serializer.data)
        # super().get(request, format)
        # TODO filter user member of place
        # queryset = self.get_queryset().filter(user=user)
        # return Response()
