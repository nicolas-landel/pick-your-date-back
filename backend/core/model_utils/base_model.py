import uuid

from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)

    class Meta:
        abstract = True
        get_latest_by = "created_at"
        ordering = ("-created_at",)
