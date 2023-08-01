from rest_framework import serializers

from .models import UsernameOsintResult, EmailOsintResult


class OsintResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsernameOsintResult
        fields = '__all__'


class EmailOsintSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOsintResult
        fields = ['email', 'results','created_at', 'updated_at']
