from rest_framework.generics import GenericAPIView as View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from core.serializers import LoginSerializer, RegisterSerializer, UserSerializer


class RegisterUserAPI(View):

    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data

        register_user_serializer = self.get_serializer(data=user_data)
        register_user_serializer.is_valid(raise_exception=True)
        register_user_serializer.save()

        return Response(register_user_serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPI(View):

    serializer_class = LoginSerializer

    def post(self, request):
        user_creds = request.data

        user_login_serializer = self.get_serializer(data=user_creds)

        user = authenticate(**user_login_serializer.data)

        if not user:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serialized_user = UserSerializer(user)

        return Response(serialized_user.data, status=status.HTTP_200_OK)


class UserProfileAPI(View):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        serialized_user = self.get_serializer(user)

        return Response(serialized_user.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user

        user_update_data = request.data

        user_update_serializer = self.get_serializer(
            user, data=user_update_data, partial=True
        )
        user_update_serializer.is_valid(raise_exception=True)
        user_update_serializer.save()

        return Response(user_update_serializer.data, status=status.HTTP_200_OK)
