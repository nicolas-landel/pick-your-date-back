from django.db import models
from django.utils.translation import gettext_lazy as _

from core.model_utils import BaseModel


class Answer(BaseModel):
    date = models.DateField()
    option = models.ForeignKey(
        "place.Option",
        null=True,
        blank=True,
        related_name="answers",
        on_delete=models.SET_NULL,
    )
    place = models.ForeignKey(
        "place.Place", related_name="answers", on_delete=models.CASCADE
    )
    is_archived = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        "user.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Created by"),
        related_name="answers",
    )

    def __str__(self):
        return f"Answer {self.uuid}"
