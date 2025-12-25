from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileUpdateRequestSerializer(serializers.Serializer):
    display_name = serializers.CharField(
        max_length=100,
        required=False,
    )
    detail = serializers.CharField(
        max_length=500,
        required=False,
        allow_blank=True,
    )
