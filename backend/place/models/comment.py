from core.model_utils import BaseModel
from django.db import models


class Comment(BaseModel):

    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    place = models.ForeignKey("place.Place", on_delete=models.CASCADE)
    reply_to = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )

    def __str__(self):
        return f"Comment {self.uuid}"
