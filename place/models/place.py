from core.model_utils import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class CountryEnum:
    FRANCE = "FRANCE"

    @classmethod
    def get_as_choices(cls):
        return [(cls.FRANCE, _(cls.FRANCE))]


class Place(BaseModel):

    name = models.CharField(max_length=255, default=_("Place"), verbose_name=_("Place"))
    address = models.TextField(default="", verbose_name=_("Address"), max_length=255)
    address_comment = models.TextField(
        blank=True, null=True, verbose_name=_("Address comment"), max_length=510
    )
    zipcode = models.CharField(
        blank=True, null=True, max_length=5, verbose_name=_("Zipcode")
    )
    city_name = models.CharField(
        blank=True, null=True, max_length=50, verbose_name=_("City name")
    )
    country_name = models.CharField(
        default=CountryEnum.FRANCE,
        max_length=50,
        choices=CountryEnum.get_as_choices(),
        verbose_name=_("Country"),
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    max_capacity = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(
        "user.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Created by"),
    )

    def __str__(self):
        return f" Place {self.name}"
