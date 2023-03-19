from django_filters import FilterSet

from place.models import Answer


class AnswerFilter(FilterSet):
    class Meta:
        model = Answer
        fields = [
            "place",
        ]
