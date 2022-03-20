from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]
        read_only_fields = [
            "last_login",
            "date_joined",
            "is_active",
            "is_staff",
            "is_superuser",
        ]

    def get_token(self, obj):
        return obj.token


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        allow_blank=False,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
