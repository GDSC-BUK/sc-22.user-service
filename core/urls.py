from django.urls import path

from core.api import RegisterUserAPI, UserLoginAPI, UserProfileAPI

app_name = "core"

urlpatterns = [
    path("register/", RegisterUserAPI.as_view(), name="user_register"),
    path("login/", UserLoginAPI.as_view(), name="user_login"),
    path("profile/", UserProfileAPI.as_view(), name="user_profile"),
]
