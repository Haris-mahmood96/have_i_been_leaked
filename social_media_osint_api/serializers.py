from rest_framework import serializers

from .models import UsernameOsintResult, EmailOsintResult


class OsintResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsernameOsintResult
        fields = '__all__'


class EmailOsintSerializer(serializers.ModelSerializer):
    basic_email_reputation = serializers.JSONField()
    leaks = serializers.JSONField()
    social_media_registrations = serializers.ListField(child=serializers.JSONField())

    class Meta:
        model = EmailOsintResult
        fields = ['email', 'basic_email_reputation', 'leaks', 'social_media_registrations', 'created_at', 'updated_at']
