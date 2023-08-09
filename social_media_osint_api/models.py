from django.db import models
from djongo import models as djongo_models


class UsernameOsintResult(models.Model):
    username = models.CharField(max_length=255)
    data = djongo_models.JSONField()

    def __str__(self):
        return self.username


class EmailOsintResult(models.Model):
    email = models.EmailField(unique=True)
    basic_email_reputation = djongo_models.JSONField(default=dict, blank=True)
    leaks = djongo_models.JSONField(default=dict, blank=True)
    social_media_registrations = djongo_models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

