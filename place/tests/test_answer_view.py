from django.test import TestCase

from place.models import Answer
from place.views import AnswerPlaceView
from user.models import Membership
from utils.tests.base_tests import (
    TestRequestFactory,
    create_default_user,
    create_place_with_data,
)


class PlaceViewTestCase(TestRequestFactory, TestCase):
    view_class = AnswerPlaceView

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = create_default_user()

    def setUp(self):
        self.place, self.options, self.answers, *_ = create_place_with_data()

    def test_list_answers_no_place(self):
        response = self.get_response(route="/places/place_answers/", data={})
        self.assertEqual(response.status_code, 403)

    def test_list_answers_user_not_member(self):
        response = self.get_response(
            route="/places/place_answers/", data={"place": str(self.place.uuid)}
        )
        self.assertEqual(response.status_code, 403)

    def test_list_answers_user_member(self):
        self.assertTrue(Answer.objects.count())
        # Create a membership for user and place, should get the answers of the place
        Membership.objects.create(place=self.place, user=self.user)
        response = self.get_response(
            route="/places/place_answers/", data={"place": str(self.place.uuid)}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
