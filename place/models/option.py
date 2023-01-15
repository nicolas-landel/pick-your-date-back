from core.model_utils import BaseModel
from django.db import models


class Option(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default="#FFFFFF")
    created_by = models.ForeignKey(
        "user.User", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"Option {self.name}"
