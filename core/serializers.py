from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

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
    password = serializers.CharField(write_only=True)
