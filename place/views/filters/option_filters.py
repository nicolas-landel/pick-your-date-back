from django_filters import FilterSet

from place.models import Option


class OptionFilter(FilterSet):
    class Meta:
        model = Option
        fields = [
            "place",
        ]
