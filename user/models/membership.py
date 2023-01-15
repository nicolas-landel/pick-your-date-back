from django.db import models
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):

    ADMIN = "admin"
    READ_ONLY = "read_only"
    EDITOR = "editor"

    ROLES = (
        (READ_ONLY, _("read only")),
        (EDITOR, _("editor")),
        (ADMIN, _("admin")),
    )

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    place = models.ForeignKey(
        "place.Place", on_delete=models.CASCADE
    )
    role = models.CharField(max_length=200, choices=ROLES, default=ADMIN)
    is_favorite = models.BooleanField(default=False)
    hide_membership = models.BooleanField(default=False)

    @classmethod
    def create_membership(cls, user, place, role, hide_membership=False):
        if cls.check_role(role):
            member = cls(user=user, place=place, role=role, hide_membership=hide_membership)
            member.save()
        else:
            raise ValueError("Role is not valid")

    @classmethod
    def check_role(cls, role_to_check):
        """
        Check that a string 'role_to_check' is a defined role (always check the 1st value of the tuple of ROLES)
        :param role_to_check: string
        :return:
        """
        list_roles = [cls.ROLES[i][0] for i in range(len(cls.ROLES))]
        return role_to_check in list_roles

    @classmethod
    def get_list_all_memberships_user(cls, user):
        """
        Get the list of all the membership of an user
        :return: list of memberships
        """
        return list(cls.objects.filter(user=user))

    def __str__(self):
        return f"{self.pk}"
