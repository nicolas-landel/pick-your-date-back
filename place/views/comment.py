from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from place.models import Comment
from place.permissions import IsMemberPlace
from place.serializers import CommentSerializer
from place.views.filters import CommentFilter


class CommentPlaceView(ListAPIView):
    permission_classes = [IsAuthenticated, IsMemberPlace]
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_class = CommentFilter
