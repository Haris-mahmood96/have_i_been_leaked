from django.db import models
from djongo import models as djongo_models


class UsernameOsintResult(models.Model):
    username = models.CharField(max_length=255)
    data = djongo_models.JSONField()

    def __str__(self):
        return self.username


class EmailOsintResult(models.Model):
    email = models.EmailField(unique=True)
    results = djongo_models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
