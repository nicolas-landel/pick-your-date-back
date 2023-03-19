from dateutil.relativedelta import relativedelta
from django.utils import timezone
from rest_framework.test import APIRequestFactory, force_authenticate

from place.models import Answer, Option, Place
from user.models import User
from user.serializers import UserCreationSerializer


class TestRequestFactory:
    user = None
    view_class = None

    def get_response(
        self,
        route="",
        data={},
    ):
        factory = APIRequestFactory()
        request = factory.get(route, data)
        force_authenticate(request, user=self.user)
        view = self.view_class.as_view()
        return view(request)


def create_default_user():
    data = {
        "first_name": "Jean",
        "last_name": "Sav",
        "email": "test@hotmail.com",
        "password": "password_test",
    }
    serializer = UserCreationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.instance


def create_place_with_data(**kwargs):
    place = Place.objects.create(name="Place", **kwargs)
    user = User.objects.first()
    options = []
    answers = []
    for i in range(3):
        option = Option.objects.create(
            place=place, name=f"Option {i+1}", created_by=user
        )
        options.append(option)
        date = timezone.now() + relativedelta(days=i)
        answer = Answer.objects.create(
            date=date, place=place, option=option, created_by=user
        )
        answers.append(answer)

    return place, options, answers
