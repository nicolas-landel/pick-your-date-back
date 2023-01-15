from core.model_utils import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Answer(BaseModel):

    date = models.DateField()
    option = models.ForeignKey(
        "place.Option", null=True, blank=True, on_delete=models.SET_NULL
    )
    place = models.ForeignKey("place.Place", on_delete=models.CASCADE)
    is_archived = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        "user.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Created by"),
    )

    def __str__(self):
        return f"Answer {self.uuid}"
