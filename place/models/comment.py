from django.db import models

from core.model_utils import BaseModel


class Comment(BaseModel):
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="comments"
    )
    answer = models.ForeignKey(
        "place.Answer",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    reply_to = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )

    def __str__(self):
        return f"Comment {self.uuid}"
