from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # repeat_words = models.IntegerField(null=True)

    def __str__(self):
        return self.username
