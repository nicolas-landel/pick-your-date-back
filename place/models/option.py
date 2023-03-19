from django.db import models

from core.model_utils import BaseModel


class Option(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default="#FFFFFF")
    place = models.ForeignKey(
        "place.Place", related_name="options", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        "user.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="options",
    )

    def __str__(self):
        return f"Option {self.name}"
