from email.policy import default
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Answer(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    option = models.ForeignKey("place.Option", null=True, blank=True, on_delete=models.SET_NULL)
    site = models.ForeignKey("place.Place", on_delete=models.CASCADE)
    is_archived = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_add=True)
    created_by = models.ForeignKey("user.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Created by"),
    )

    def __str__(self):
        return f"Answer {self.uuid}"