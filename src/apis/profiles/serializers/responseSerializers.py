from rest_framework import serializers
from src.models.profile import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "user_id",
            "display_name",
            "detail",
        ]


class UserProfileResponseSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "profile",
        ]
