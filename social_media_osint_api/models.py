from django.db import models
from djongo import models as djongo_models


class OsintResult(models.Model):
    username = models.CharField(max_length=255)
    data = djongo_models.JSONField()

    def __str__(self):
        return self.username
