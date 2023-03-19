from django_filters import FilterSet

from place.models import Comment


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = [
            "answer__place",
        ]
