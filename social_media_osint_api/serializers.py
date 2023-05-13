from rest_framework import serializers
from .models import OsintResult


class OsintResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsintResult
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)