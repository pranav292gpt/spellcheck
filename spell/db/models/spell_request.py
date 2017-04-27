from django.db import models
import uuid

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    response = models.TextField()
    feedback = models.TextField(null=True)
