from rest_framework import serializers
from .models import OsintResult


class OsintResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsintResult
        fields = '__all__'
