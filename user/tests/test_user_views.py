from django.test import TestCase

from user.models import Membership
from user.views import ListUserMembers
from utils.tests.base_tests import (
    TestRequestFactory,
    create_default_user,
    create_place_with_data,
)

# Create your tests here.


class ListUserMembersViewTestCase(TestRequestFactory, TestCase):
    view_class = ListUserMembers

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = create_default_user()
        cls.place, cls.options, cls.answers, *_ = create_place_with_data()

    def test_list_place_members_not_member(self):
        response = self.get_response(
            route="/users/members/", data={"place": str(self.place.uuid)}
        )
        self.assertEqual(response.status_code, 403)

    def test_list_place_members(self):
        self.assertEqual(len(self.place.members.all()), 0)
        Membership.objects.create(place=self.place, user=self.user)
        response = self.get_response(
            route="/users/members/", data={"place": str(self.place.uuid)}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], self.user.first_name)
        self.assertEqual(response.data[0]["last_name"], self.user.last_name)
        self.assertEqual(response.data[0]["email"], self.user.email)
