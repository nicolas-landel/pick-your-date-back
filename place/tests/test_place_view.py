from django.test import TestCase

from place.models import Place
from place.views import PlaceListView
from user.models import Membership
from utils.tests.base_tests import (
    TestRequestFactory,
    create_default_user,
    create_place_with_data,
)


class PlaceViewTestCase(TestRequestFactory, TestCase):
    view_class = PlaceListView

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = create_default_user()

    def setUp(self):
        self.place, self.options, self.answers, *_ = create_place_with_data()

    def test_list_places_not_member(self):
        response = self.get_response(route="/places/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_list_places_user_member(self):
        self.assertEqual(Place.objects.count(), 1)
        # Create a membership for user and place, should get the place with the call
        Membership.objects.create(place=self.place, user=self.user)
        response = self.get_response(route="/places/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get("uuid"), str(self.place.uuid))
