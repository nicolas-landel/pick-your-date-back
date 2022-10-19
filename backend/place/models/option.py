from django.db import models
import uuid


class Option(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default="#FFFFFF")
    created_by = models.ForeignKey("user.User", null=True, blank=True, on_delete=models.SET_NULL)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_add=True)

    def __str__(self):
        return f"Option {self.name}"