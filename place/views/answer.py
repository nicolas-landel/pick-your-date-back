from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from place.models import Answer
from place.permissions import IsMemberPlace
from place.serializers import AnswerSerializer
from place.views.filters import AnswerFilter


class AnswerPlaceView(ListAPIView):
    permission_classes = [IsAuthenticated, IsMemberPlace]
    model = Answer
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    filterset_class = AnswerFilter
