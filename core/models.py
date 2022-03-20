from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from random_username.generate import generate_username

from user.utils import BaseModel


class User(AbstractUser, BaseModel):
    class TYPES(models.TextChoices):
        NORMAL = "NR", "Normal"
        THERAPIST = "TH", "Therapist"

    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField(max_length=150, null=True)
    type = models.CharField(max_length=10, choices=TYPES.choices, default=TYPES.NORMAL)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        ordering = ["-pk"]

    def save(self, *args, **kwargs):
        if not self.username:
            username_is_unique = False

            while not username_is_unique:
                username = generate_username(1)[0]
                username_exists = User.objects.filter(username=username).exists()

                if not username_exists:
                    username_is_unique = True

                    self.username = username

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def token(self):
        user = User.objects.get(id=self.id)
        token, _ = Token.objects.get_or_create(user=user)

        return token.key
