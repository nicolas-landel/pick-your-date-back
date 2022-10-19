from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Place(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        default=_("Place"),
        verbose_name=_("Place")
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    max_capacity = models.IntegerField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_by = models.ForeignKey("user.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Created by"),
    )

    def __str__(self):
        return f" Place {self.name}"
