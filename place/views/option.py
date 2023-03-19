from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from place.models import Option
from place.permissions import IsMemberPlace
from place.serializers import OptionSerializer
from place.views.filters import OptionFilter


class OptionPlaceView(ListAPIView):
    permission_classes = [IsAuthenticated, IsMemberPlace]
    model = Option
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    filterset_class = OptionFilter
