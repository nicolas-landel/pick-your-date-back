import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True)
    updated_at = models.DateTimeField(db_index=True)

    class Meta:
        abstract = True
        get_latest_by = "created_at"
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created_at and self._state.adding:
            self.created_at = now
        if self.updated_at:
            self.updated_at = now
        return super().save(*args, **kwargs)
